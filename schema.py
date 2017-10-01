# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import (db_session,
                    User as UserModel, CredentialProfiles as CpModel)


class CPs(SQLAlchemyObjectType):
    class Meta:
        model = CpModel
        interfaces = (relay.Node, )


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
        id = UserModel.id


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(Users)
    credential_profiles = SQLAlchemyConnectionField(CPs)
    find_by_id = graphene.Field(lambda: Users, id=graphene.Int())
    find_by_username = graphene.Field(lambda: Users, username=graphene.String())

    def resolve_find_by_id(self, args, context, info):
        query = Users.get_query(context)
        user_id = args['id']
        return query.filter(UserModel.id == user_id).first()

    def resolve_find_by_username(self, args, context, info):
        query = Users.get_query(context)
        username = args['username']
        return query.filter(UserModel.username == username).first()


# region mutations


class CreateUser(graphene.Mutation):
    class Input:
        name = graphene.String()
        username = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    @classmethod
    def mutate(cls, _, args, context, info):
        user = UserModel(name=args['name'], username=args['username'])
        db_session.add(user)
        db_session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)
        return CreateUser(user=user, ok=ok)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

# endregion


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Users, CPs])
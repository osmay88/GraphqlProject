from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class CredentialProfiles(Base):
    __tablename__ = 'credentials_profiles'
    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.now())
    user_id = Column(ForeignKey('users.id'))



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True)
    credential_profiles = relationship(CredentialProfiles, backref=backref('user', cascade='delete,all'))





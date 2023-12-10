from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import os

database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.db")
engine = create_engine("sqlite:///" + database_file, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))
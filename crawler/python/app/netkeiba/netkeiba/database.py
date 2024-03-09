from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import config

USER = config.DB_USER
PASSWORD = config.PASSWORD
HOST = config.HOST
DB_NAME= config.DATABASE

ENGINE = create_engine(
    f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DB_NAME}',
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()

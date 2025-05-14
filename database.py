from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
engine = create_engine("mysql://root:.@localhost:3306/test2")

def create_database():
    Base.metadata.create_all(engine)

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def get_engine():
    return engine

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.models import Base

def get_engine():
    return create_engine('sqlite:///maintenance.db')  
def create_tables(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:yehia@localhost:5432/postgres")
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
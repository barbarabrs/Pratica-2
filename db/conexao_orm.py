from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/postgres")

Session = sessionmaker(bind=engine)

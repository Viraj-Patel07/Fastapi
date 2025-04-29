from sqlalchemy import create_engine

postgresql_database_url = "postgresql://postgres:@viraj1@localhost:5432/"

engine = create_engine(postgresql_database_url)
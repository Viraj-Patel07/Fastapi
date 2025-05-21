from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:%40viraj1%40@localhost:5432/Blog"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# def test_connection():
#     db = SessionLocal()
#     try:
#         result = db.execute(text("SELECT current_database();"))
#         db_name = result.fetchone()[0]
#         print(f"Connected to database: {db_name}")
#     except Exception as e:
#         print(f"Failed to connect to database: {e}")
#     finally:
#         db.close()
# test_connection()
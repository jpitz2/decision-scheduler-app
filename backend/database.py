# Connection to SQLite database using SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Define database URL
DATABASE_URL = "sqlite:///./planner.db"

# 2. Create engine/ connection to database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) 

# 3. Create SessionLocal class
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create Base class
Base = declarative_base()

# 5.  Create helper function to get db session
def get_db():
    db = SessionLocal()   
    try:
        yield db
    finally:
        db.close()

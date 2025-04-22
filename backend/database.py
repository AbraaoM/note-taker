from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection URL from environment variable
DATABASE_URL = getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost/notes')

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create tables
def create_tables():
    from models.user_database_model import Base as UserBase
    from models.note_database_model import Base as NoteBase
    
    UserBase.metadata.create_all(bind=engine)
    NoteBase.metadata.create_all(bind=engine)

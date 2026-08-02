from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from app.config.settings import settings
from app.database.base import Base

DATABASE_URL=settings.DATABASE_URL

engine=create_engine(DATABASE_URL,future=True,pool_pre_ping=True)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)
    
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
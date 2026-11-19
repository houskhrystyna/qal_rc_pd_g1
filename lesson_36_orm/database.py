import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/your_database"

engine = create_engine(
    DATABASE_URL,
    echo=False,  # Встановити True для дебагу
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
    
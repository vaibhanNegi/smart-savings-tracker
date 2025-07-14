# database.py

from sqlalchemy import create_engine

# PostgreSQL credentials
DATABASE_NAME = "smart_saving_db"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

# Create SQLAlchemy engine
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE_NAME}"
)

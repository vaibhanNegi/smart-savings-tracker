# db_utils.py

from sqlalchemy import create_engine
import pandas as pd

# DB connection function
def get_engine():
    # Replace these with your actual PostgreSQL credentials
    username = "postgres"
    password = "1234"
    host = "localhost"
    port = "5432"
    database = "smart_savings_db"  # Replace with your DB name

    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
    return engine

# Save data to DB
def save_data_to_db(df, table_name):
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists='append', index=False)

# Read data from DB
def read_data_from_db(query):
    engine = get_engine()
    return pd.read_sql(query, engine)

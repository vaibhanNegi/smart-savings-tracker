from sqlalchemy import create_engine, text

# Replace with your actual values
username = 'postgres'
password = '1234'
host = 'localhost'
port = '5432'
database = 'smart_saving_db'

# PostgreSQL connection URI
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Create SQLAlchemy engine
engine = create_engine(connection_string)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.fetchone()
        print(f"✅ Connected successfully!\nPostgreSQL version: {version[0]}")
except Exception as e:
    print(f"❌ Error connecting: {e}")

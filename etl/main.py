import pandas as pd
import os
from sqlalchemy import create_engine

# Load CSVs
sales = pd.read_csv('data/sales.csv')
balance = pd.read_csv('data/balance.csv')

# Clean data
sales['date'] = pd.to_datetime(sales['date'])
balance['date'] = pd.to_datetime(balance['date'])

# Database connection
db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(db_url)

# Load to PostgreSQL
sales.to_sql('sales', engine, if_exists='replace', index=False)
balance.to_sql('balance', engine, if_exists='replace', index=False)

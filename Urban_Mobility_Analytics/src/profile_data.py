from sqlalchemy import create_engine
import pandas as pd

# Database Configuration
USERNAME = "abhishekmahto"
PASSWORD = "PASSWORD"
HOST = "localhost"
PORT = "5432"
DATABASE = "urban_mobility_analytics"

# Create Engine
engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# -----------------------------
# Functions
# -----------------------------

def load_data(engine, table_name):
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, engine)


def profile_dataset(df):
    print("\nShape:")
    print(df.shape)

    print("\nInfo:")
    df.info()

    print("\nSummary Statistics:")
    print(df.describe(include="all"))

    print("\nMissing Values:")
    print(df.isnull().sum())


# -----------------------------
# Main Program
# -----------------------------

with engine.connect():
    print("Connected to the database successfully!")

query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
"""

tables_df = pd.read_sql(query, engine)

print("\nTables in Database:")
print(tables_df)

# First table name
first_table = tables_df["table_name"].iloc[0]

print(f"\nLoading Table: {first_table}")

# Load Data
df = load_data(engine, first_table)

# Profile Dataset
profile_dataset(df)
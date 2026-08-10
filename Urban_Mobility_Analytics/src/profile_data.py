from sqlalchemy import create_engine
import pandas as pd

# -----------------------------
# Database Configuration
# -----------------------------

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
    query = f'SELECT * FROM "{table_name}";'
    return pd.read_sql(query, engine)


def profile_dataset(df):

    print("\n" + "=" * 50)
    print("DATASET PROFILING")
    print("=" * 50)

    # 1. Shape
    print("\nShape:")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # 2. Data Types
    print("\nData Types:")
    print(df.dtypes)

    # 3. Missing Values
    print("\nMissing Values:")

    missing = df.isnull().sum()
    missing_percentage = (missing / len(df)) * 100

    missing_report = pd.DataFrame({
        "Missing_Count": missing,
        "Missing_Percentage": missing_percentage.round(2)
    })

    print(missing_report)

    # 4. Duplicate Rows
    print("\n Duplicate Rows:")
    print(df.duplicated().sum())

    # 5. Unique Values
    print("\n Unique Values:")
    print(df.nunique())

    # 6. Summary Statistics
    print("\n Summary Statistics:")
    print(df.describe(include="all"))


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

# Select first table
first_table = tables_df["table_name"].iloc[0]

print(f"\nLoading Table: {first_table}")


#MAKING A FUNCTION CLEAN_DATASET IN WHICH REMOVE THE NULL VALUES OF DATASET AND MAKING FEATURE ENGINEERING

def clean_dataset(df):
    print("\n" + "=" *50)
    print("CLEANING DATASET")
    print("=" * 50)


#1.REMOVE COMPLETELY EMPTY COLUMNS
    empty_cols = df.columns[df.isnull().all().tolist()]
    print("/n Removing the empty columns ")
    print(empty_cols)


    df = df.dropna(axis=1,how="all")
    print("\n Shape of the dataset after removing the empty columns:")
    print(df.shape)


#2.Remove duplicate Rows
    duplicated_rows = df.duplicated().sum()
    print(f"\n Number of duplicated rows: {dupicated_rows}")
    df = df.drop_duplicates().copy()
    print(f"\n Rows after removing duplicates : {len(df)}")


    return df




# Load Data
df = load_data(engine, first_table)

# Profile Dataset
profile_dataset(df) 

cleaned_df = clean_dataset(df)



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


#lets make data cleaning function to remove the useless columns and remove the duplcate rows and column

def clean_dataset(df):
    print("\n" + "=" * 50)
    print("\n Cleaning Dataset")
    print("=" * 50)


#1.remove columns whose are emplty or have more than 50% missing values

    empty_columns = df.columns[df.isnull().isnull().all().tolist()]
    print("\n Empty Columns:")
    print(empty_columns)

    df = df.dropna(axis=1, how='all')  # Drop empty columns



#2.CONVERT THE DATE AND TIME COLUMNS INTO THEIR APPROPRIATE DATA TYPES
    df["DATE"]=pd.to_datetime(df["DATE"], errors= "coerce")


#3.CONVERT DATETIME COLUMNS INTO ITS APPROPRIATE DATA TYPE
    df["TIME"]=pd.to_datetime(df["TIME"], format="%I:%M:%S %p", errors= "coerce").dt.time

    print("\nData Types after cleaning:")
    print(df.dtypes)


    print("\n Now the new cleaned dataset shape is :")
    print(df.shape)



    #4.REMOVE THE DUPLICATED ENTRIES
    duplicates_before = df.duplicated().sum()
    print(f"\n  Duplicate Rows before cleaning: {duplicates_before}")
    df = df.drop_duplicates()


    print(f"\n Rows after removing Duplicates: {len(df)}")


    #validation
    print("\n Final data type:")
    print(df.dtypes)


    print("\n Final Shape of the dataset:")
    print(df.shape)

    print("\n Missing values after cleaning:")
    print(df.isnull().sum())

    return df




# Load Data
df = load_data(engine, first_table)

# Profile Dataset
profile_dataset(df)

cleaned_df = clean_dataset(df)



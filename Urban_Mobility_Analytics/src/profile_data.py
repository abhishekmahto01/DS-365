from sqlalchemy import create_engine
import pandas as pd


USERNAME = "abhishekmahto"
PASSWORD = "PASSWORD"
HOST="localhost"
PORT="5432"
DATABASE="urban_mobility_analytics"

engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

folder = "/Users/abhishekmahto/Desktop/archive (4)"


with engine.connect() as connection:
    print("Connected to the database successfully!")


query = """
select table_name
from information_schema.tables
where table_schema ='public';
"""

tables_df=pd.read_sql(query,engine)
print("Tables in Database:")

first_table = tables_df["table_name"].iloc[0]

print(first_table)





query = """
SELECT *
FROM other_american_b01362;
"""

df = pd.read_sql(query, engine)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())
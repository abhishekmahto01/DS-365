import os
import pandas as pd
from sqlalchemy import create_engine

USERNAME = "abhishekmahto"
PASSWORD = "YOUR_POSTGRES_PASSWORD"
HOST = "localhost"
PORT = "5432"
DATABASE = "urban_mobility_analytics"

engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

folder = "/Users/abhishekmahto/Desktop/archive (4)"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        table_name = (
            os.path.splitext(file)[0]
            .replace("-", "_")
            .replace(" ", "_")
            .lower()
        )

        print(f"Importing {file} → {table_name}")

        encodings = ["utf-8", "latin1", "cp1252", "ISO-8859-1"]

        df = None

        for enc in encodings:
            try:
                df = pd.read_csv(path, encoding=enc)
                print(f"✅ {file} loaded with {enc}")
                break
            except UnicodeDecodeError:
                pass

        if df is None:
            print(f"❌ Could not read {file}")
            continue

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

print("🎉 All CSV files imported successfully!")
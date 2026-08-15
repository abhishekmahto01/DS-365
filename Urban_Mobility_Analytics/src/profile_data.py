from sqlalchemy import create_engine
import pandas as pd


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

USERNAME = "abhishekmahto"
PASSWORD = "PASSWORD"
HOST = "localhost"
PORT = "5432"
DATABASE = "urban_mobility_analytics"


# Create database engine
engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)


# ============================================================
# 1. GET ALL TABLES
# ============================================================

def get_tables(engine):

    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
      AND table_type = 'BASE TABLE'
    ORDER BY table_name;
    """

    tables_df = pd.read_sql(query, engine)

    return tables_df


# ============================================================
# 2. LOAD A TABLE
# ============================================================

def load_data(engine, table_name):

    query = f'SELECT * FROM "{table_name}";'

    df = pd.read_sql(query, engine)

    return df


# ============================================================
# 3. PROFILE ONE TABLE
# ============================================================

def profile_table(df, table_name):

    profile_records = []

    row_count = len(df)

    for column in df.columns:

        data_type = str(df[column].dtype)

        null_count = df[column].isnull().sum()

        null_percentage = (
            (null_count / row_count) * 100
            if row_count > 0
            else 0
        )

        unique_count = df[column].nunique(
            dropna=True
        )

        # Get a few sample values
        sample_values = (
            df[column]
            .dropna()
            .astype(str)
            .unique()[:5]
            .tolist()
        )

        profile_records.append({

            "table_name": table_name,

            "column_name": column,

            "data_type": data_type,

            "row_count": row_count,

            "null_count": null_count,

            "null_percentage": round(
                null_percentage,
                2
            ),

            "unique_count": unique_count,

            "sample_values": sample_values
        })

    return pd.DataFrame(profile_records)


# ============================================================
# 4. PROFILE ALL TABLES
# ============================================================

def profile_all_tables(engine, tables_df):

    all_profiles = []

    total_tables = len(tables_df)

    print("\n" + "=" * 70)
    print("STARTING DATA DISCOVERY")
    print("=" * 70)

    print(
        f"\nTotal tables found: {total_tables}"
    )

    for index, row in tables_df.iterrows():

        table_name = row["table_name"]

        print("\n" + "-" * 70)

        print(
            f"Processing table {index + 1}/{total_tables}: "
            f"{table_name}"
        )

        print("-" * 70)

        try:

            # Load table
            df = load_data(
                engine,
                table_name
            )

            print(
                f"Rows    : {df.shape[0]}"
            )

            print(
                f"Columns : {df.shape[1]}"
            )

            # Profile table
            table_profile = profile_table(
                df,
                table_name
            )

            all_profiles.append(
                table_profile
            )

            print(
                "✓ Profiling completed"
            )

        except Exception as e:

            print(
                f"✗ Error processing {table_name}"
            )

            print(
                f"Error: {e}"
            )

    # Combine all table profiles
    if all_profiles:

        profile_df = pd.concat(
            all_profiles,
            ignore_index=True
        )

    else:

        profile_df = pd.DataFrame()

    return profile_df


# ============================================================
# 5. MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    try:

        # ----------------------------------------------------
        # DATABASE CONNECTION
        # ----------------------------------------------------

        with engine.connect():

            print(
                "\n✓ Connected to PostgreSQL successfully!"
            )


        # ----------------------------------------------------
        # GET TABLES
        # ----------------------------------------------------

        tables_df = get_tables(
            engine
        )


        print("\n" + "=" * 70)
        print("TABLES IN DATABASE")
        print("=" * 70)

        print(
            tables_df.to_string(
                index=False
            )
        )


        # ----------------------------------------------------
        # PROFILE ALL TABLES
        # ----------------------------------------------------

        profile_df = profile_all_tables(
            engine,
            tables_df
        )


        # ----------------------------------------------------
        # FINAL DISCOVERY REPORT
        # ----------------------------------------------------

        print("\n" + "=" * 70)
        print("DATA DISCOVERY COMPLETED")
        print("=" * 70)

        print(
            f"\nTotal tables profiled: "
            f"{profile_df['table_name'].nunique()}"
        )

        print(
            f"Total columns discovered: "
            f"{len(profile_df)}"
        )


        # ----------------------------------------------------
        # DISPLAY PROFILE
        # ----------------------------------------------------

        print("\n" + "=" * 70)
        print("COLUMN-LEVEL DATA PROFILE")
        print("=" * 70)

        print(
            profile_df.to_string(
                index=False
            )
        )


        # ----------------------------------------------------
        # STORE IN PYTHON MEMORY
        # ----------------------------------------------------

        print("\n" + "=" * 70)
        print("AVAILABLE PYTHON OBJECTS")
        print("=" * 70)

        print(
            "\ntables_df  → List of database tables"
        )

        print(
            "profile_df → Column-level profiling information"
        )

        print(
            "\nNo database tables were created or modified."
        )


    except Exception as e:

        print(
            "\n✗ Database connection failed!"
        )

        print(
            f"Error: {e}"
        )

        
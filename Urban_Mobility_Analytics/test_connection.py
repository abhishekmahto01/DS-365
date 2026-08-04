from  sqlalalchemy import create_engine


USERNAME = "abhishekmahto"     
PASSWORD = "Abhi@123456789"
HOST = "localhost"
PORT = "5432"
DATABASE = "urban_mobility_analytics"


engine = create_engine(f"postgreyql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    f"postgreysql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )


with engine.connect() as connection:
    print("postrey connected successfully")                                         
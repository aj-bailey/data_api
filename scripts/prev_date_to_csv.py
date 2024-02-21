from datetime import datetime, timedelta

import pandas as pd
import psycopg2
from environs import Env

env = Env()
env.read_env(".env")

db_params = {
    "host": env.str("DATABASE_HOST"),
    "database": env.str("POSTGRES_DB"),
    "user": env.str("POSTGRES_USER"),
    "password": env.str("POSTGRES_PASSWORD")
}

today = datetime.now()
today_str = today.strftime('%Y-%m-%d')
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')

query = f"SELECT * FROM dhtreadings WHERE created_at::date = '{yesterday_str}'"

try:
    conn = psycopg2.connect(**db_params)
    df = pd.read_sql_query(query, conn, index_col='id')
    df.to_csv(f"/home/adam.bailey/Desktop/apps/data_api/scripts/{yesterday_str}_data.csv")

except (Exception, psycopg2.Error) as error:
    print("Error:", error)

finally:
    if conn:
        conn.close()

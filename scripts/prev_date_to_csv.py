import psycopg2
import pandas as pd
from datetime import datetime, timedelta

# Database connection parameters
db_params = {
    "host": "localhost",         # Replace with your database host
    "database": "dht", # Replace with your database name
    "user": "postgres",         # Replace with your database user
    "password": "postgres"  # Replace with your database password
}

# Calculate previous date
today = datetime.now()
today_str = today.strftime('%Y-%m-%d')
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')

# SQL query to retrieve humidity, temperature, and timesta
query = f"SELECT * FROM dhtreadings WHERE created_at::date = '{yesterday_str}'"

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    df = pd.read_sql_query(query, conn, index_col='id')

    df.to_csv(f"/home/adam.bailey/Desktop/apps/data_api/scripts/{yesterday_str}_data.csv")

except (Exception, psycopg2.Error) as error:
    print("Error:", error)

finally:
    # Close the database connection and cursor
    # if cursor:
    #     cursor.close()
    if conn:
        conn.close()

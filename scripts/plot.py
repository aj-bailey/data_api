import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Database connection parameters
db_params = {
    "host": "localhost",         # Replace with your database host
    "database": "dht", # Replace with your database name
    "user": "postgres",         # Replace with your database user
    "password": "postgres"  # Replace with your database password
}

# SQL query to retrieve humidity, temperature, and timesta
query = "SELECT created_at, humidity, temperature FROM dhtreadings"

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the rows from the result set and load into a Pandas DataFrame
    data = cursor.fetchall()
    columns = ["created_at", "humidity", "temperature"]
    df = pd.DataFrame(data, columns=columns)

    # Convert the "timestamp" column to a datetime object
    df["created_at"] = pd.to_datetime(df["created_at"])

    # df.to_csv("temp_hum_data.csv")
    # Plot for Humidity
    plt.subplot(2, 1, 1)
    plt.plot(df["created_at"], df["humidity"], label="Humidity", linestyle='-', color='green')
    plt.xlabel("Timestamp")
    plt.ylabel("Humidity")
    plt.title("Humidity Over Time")
    plt.legend()
    plt.grid()

    # Plot for Temperature
    plt.subplot(2, 1, 2)
    plt.plot(df["created_at"], df["temperature"], label="Temperature", linestyle='-', color='red')
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature")
    plt.title("Temperature Over Time")
    plt.legend()
    plt.grid()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust subplot spacing
    plt.tight_layout()

    # Show the plots
    plt.show()
except (Exception, psycopg2.Error) as error:
    print("Error:", error)

finally:
    # Close the database connection and cursor
    if cursor:
        cursor.close()
    if conn:
        conn.close()

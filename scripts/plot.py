from environs import Env
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

env = Env()
env.read_env(".env")

db_params = {
    "host": env.str("DATABASE_HOST"),
    "database": env.str("POSTGRES_DB"),
    "user": env.str("POSTGRES_USER"),
    "password": env.str("POSTGRES_PASSWORD")
}

query = "SELECT created_at, humidity, temperature FROM dhtreadings"

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    
    columns = ["created_at", "humidity", "temperature"]
    df = pd.DataFrame(data, columns=columns)
    df["created_at"] = pd.to_datetime(df["created_at"])

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
    
    plt.show()
except (Exception, psycopg2.Error) as error:
    print("Error:", error)

finally:
    # Close the database connection and cursor
    if cursor:
        cursor.close()
    if conn:
        conn.close()

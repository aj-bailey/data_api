import boto3
from datetime import datetime, timedelta
import os

# Calculate previous date
today = datetime.now()
today_str = today.strftime('%Y-%m-%d')
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')

# Get the absolute path of the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to your CSV file
csv_file_path = os.path.join(script_dir, f'{yesterday_str}_data.csv')

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

# The name of your S3 bucket
bucket_name = 'iot-daily-values'

# The path to your file on your local computer

# The name you want to give your file in S3
s3_file_name = '2024-02-15_data.csv'

# Upload the file
s3.upload_file(csv_file_path, bucket_name, s3_file_name)

print(f"File uploaded successfully to {bucket_name}/{s3_file_name}")

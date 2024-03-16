import os
from datetime import datetime, timedelta

import boto3


def upload_prev_date_data():
    today = datetime.now()
    today_str = today.strftime('%Y-%m-%d')
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_dir, f'{yesterday_str}_data.csv')

    s3 = boto3.client('s3')
    bucket_name = 'iot-daily-values'
    s3_file_name = f'{yesterday.year}/{yesterday.month}/{yesterday_str}_data.csv'

    s3.upload_file(csv_file_path, bucket_name, s3_file_name)

    print(f"File uploaded successfully to {bucket_name}/{s3_file_name}")

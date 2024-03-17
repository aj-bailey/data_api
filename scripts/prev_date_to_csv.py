from datetime import datetime, timedelta

import pandas as pd
from sqlalchemy import func, select

from app.config import SessionLocal
from app.model import DHTReading


def prev_date_to_csv():
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    stmt = select(DHTReading).where(func.date(DHTReading.created_at) == str(yesterday.date()))

    df = pd.read_sql(stmt, SessionLocal().bind)
    df.to_csv(f"/home/adam.bailey/Desktop/apps/data_api/scripts/{yesterday.date()}_data.csv")

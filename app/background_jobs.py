from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from scripts.prev_date_to_csv import prev_date_to_csv
from scripts.upload_csv_data import upload_prev_date_data


def schedule_jobs():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(prev_date_to_csv, CronTrigger(hour=0, minute=15))
    print("Added prev_date_to_csv to run daily at 00:15")

    scheduler.add_job(upload_prev_date_data, CronTrigger(hour=0, minute=30))
    print("Added upload_prev_date_data to run daily at 00:30")
    
    scheduler.start()
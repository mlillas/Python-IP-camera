import time
import manager
from apscheduler.schedulers.blocking import BlockingScheduler
from config import interval

def callScripts():
    print("Renameing")
    manager.rename()
    print("Starting FTP Upload")
    manager.ftpUpload()

scheduler = BlockingScheduler()
scheduler.add_job(callScripts, 'interval', minutes=interval)
scheduler.start()
import sqlite3
from uuid import uuid1
from datetime import datetime

def init(this, file, table_name):
    this.file = file
    this.table = table_name
    connect = sqlite3.connect(str(file))
    connect.close()
    
def current_time(this):
    times = datetime.now()

    year = times.year
    month = times.month
    day = times.day

    hour = times.hour
    minute = times.minute
    second = times.second
    
    if len(str(minute)) < 2:
        minute = f"0{minute}"

    if len(str(hour)) < 2:
        hour = f"0{hour}"

    mod_time = f"{year}/{month}/{day}/{hour}/{minute}/{second}"
    return mod_time

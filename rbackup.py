#!/usr/bin/env python3
import datetime
import shutil
from time import sleep

while True:
    try:
        hr = datetime.datetime.now().hour
        src = '/var/lib/redis/dump.rdb'
        dst = '/opt/redis_backup/backups/rdump_%s.rdb' % hr
        print(f"{datetime.datetime.now()} - Creating backup file: {dst}")
        shutil.copy(src, dst)
        sleep(3600)
    except Exception as exc:
        print(f"Error creating backup file: {exc}")

#!/usr/bin/env python3
import datetime
import shutil
from time import sleep

while True:
    try:
        hr = datetime.datetime.now().hour

        # Edit source file name here IF needed:
        # You might need this if you renamed the persistence file in redis.conf
        src = '/var/lib/redis/dump.rdb'

        # Edit destination file name if you prefer something different then
        # rdump_14, where the number indicates the hour of the backup
        dst = '/opt/redis_backup/backups/rdump_%s.rdb' % hr

        # This line provides logged output in syslog.
        print(f"{datetime.datetime.now()} - Creating backup file: {dst}")
        shutil.copy(src, dst)
        sleep(3600)
    except Exception as exc:
        print(f"Error creating backup file: {exc}")

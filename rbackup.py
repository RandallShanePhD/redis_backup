#!/usr/bin/env python3
import datetime
import shutil
from time import sleep

# NOTE:  this VERY simple script makes an
#  hourly copy of the redis persistence file.
#  Modify the source and destination values below.

while True:
    hr = datetime.datetime.now().hour
    src = '/var/lib/redis/dump.rdb'
    dst = '/opt/redis_backup/backups/rdump_%s.rdb' % hr
    shutil.copy(src, dst)
    sleep(3600)

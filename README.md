# redis_backup
Simple hourly redis persistence file backup service for Ubuntu servers. 
NOTE: the intent of this service is to VERY SIMPLY make a copy of your 
existing redis persistence file every hour. They overwrite meaning you 
always have only 1 day worth of files. IF you renamed your persistence 
file in redis.conf, then make sure you adjust the name in the rbackup.py
file. You can also adjust the output file name if desired.

## Make it a Service
0. As ROOT, clone, copy or deploy this repo to /opt directory.
   * Assure the directory is names redis_backup
   * sudo mv /opt/redis_backup* /opt/redis_backup
   * Owned/Group:  root root    Permission: 755
   * Adjust if needed with:
   * sudo chown root redis_backup/
   * sudo chgrp root redis_backup/
   * sudo chmod 755 redis_backup/
1. Create a symbolic link to the service file in /etc/systemd/system
   * sudo ln -s /opt/redis_backup/rbackup.service rbackup.service
2. Make sure that your script is executable with:
   * sudo chmod u+x /opt/redis_backup/rbackup.py
3. Edit the rbackup.py and change src & dest file names as desired
   * Necessary only IF you have renamed your persistence file
   * Else backups will be by default in /opt/redis_backup
3. Reload systemctl
   * sudo systemctl daemon-reload
4. Start it
   * sudo service rbackup start
5. Check it
   * sudo service rbackup status
6. Enable it to run at boot:
   * sudo systemctl enable rbackup

*Done - you now have hourly backup files!*

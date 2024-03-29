# redis_backup
Simple hourly redis persistence file backup service for Ubuntu servers. 
NOTE: the intent of this service is to VERY SIMPLY make a copy of your 
existing redis persistence file every hour. They overwrite meaning you 
always have only 1 day worth of files. IF you renamed your persistence 
file in redis.conf, then make sure you adjust the name in the rbackup.py
file. You can also adjust the output file name if desired.

## Make it a Service
0. As ROOT, clone this repo to /opt directory.
1. Copy the rbackup.service file to /etc/systemd/system folder
   * Assure it is named rbackup.service
2. Make sure that your script is executable with:
   * chmod u+x /opt/redis_backup/rbackup.py
3. Edit the rbackup.py and change src & dest file names as desired
   * Necessary only IF you have renamed your persistence file
3. Reload systemctl
   * sudo systemctl daemon-reload
4. Start it
   * sudo service rbackup start
5. Check it
   * sudo service rbackup status
6. Enable it to run at boot:
   * sudo systemctl enable rbackup

*Done!*

# redis_backup
Simple hourly redis persistence file backup service.

## Make it a Service
1. Copy the rbackup.service file to /etc/systemd/system folder
   * Assure it is named rbackup.service
2. Make sure that your script is executable with:
   * chmod u+x /path/to/rbackup.py
3. Edit the rbackup.py and change file names
   * Only IF you have renamed your persistence file
3. Reload systemctl
   * sudo systemctl daemon-reload
4. Start it
   * sudo service rbackup start
5. Check it
   * sudo service rbackup status
6. Enable it to run at boot:
   * sudo systemctl enable rbackup

*Done!*

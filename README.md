# redis_backup
Simple hourly redis persistence file backup service.

# Make it a Service
(1) Place it in /etc/systemd/system folder and name it rbackup.service
(2) Make sure that your script is executable with:
    chmod u+x /path/to/rbackup.py
(3) Start it:
    sudo systemctl start rbackup

(4) Enable it to run at boot:
    sudo systemctl enable rbackup

(5) Stop it:
    sudo systemctl stop rbackup

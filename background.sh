#!/bin/bash
printf "[Unit]\nDescription=Data Collection\nAfter=multi-user.target" > /lib/systemd/system/collectdata.service
printf "\n\n\n[Service]\nType=idle\nExecStart=\nUser=pi" > /lib/systemd/system/collectdata.service
printf "\n\n\n[Install]\nWantedBy=multi-user.target" > /lib/systemd/system/collectdata.service
cat /lib/systemd/system/collectdata.service
sudo chmod 644 /lib/systemd/system/collectdata.service
sudo systemctl daemon-reload
# start the service using sudo systemctl start collectdata.service
# stop the service using sudo systemctl stop collectdata.service

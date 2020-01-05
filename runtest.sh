#!/usr/bin/env bash
echo 'script running' >> cron.log
source /home/tasty/speedtester/bin/activate
echo 'set source' >> cron.log
cd /home/tasty/OneDrive/Documents/projects/speedtestPi
echo 'directory changed' >> cron.log
python speedtester.py
echo 'tested speed' >> cron.log

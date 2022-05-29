#!/bin/bash
service cron start
python src/main.py
service cron reload
while true
do
  sleep 1000
done

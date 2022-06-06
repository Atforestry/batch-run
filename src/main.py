import sys
import os
sys.path.insert(1, './src')

from crontab import CronTab
import time
import os

import logging
from logging.config import dictConfig
from log_config import log_config 

dictConfig(log_config)
logger = logging.getLogger("capstone") # should be this name unless you change it in log_config.py

cron = CronTab(user='root')
cron.remove_all()
job = cron.new(command='/bin/bash -c "/usr/local/bin/python /usr/src/app/src/job.py"')
job.clear()
job.env['FETCH_DATA_URL'] = os.environ['FETCH_DATA_URL']
job.hour.on(1)
job.minute.on(0)

cron.write()

logger.info('Executed main.py')

crontabCfg = os.system("crontab -l")
logger.info(crontabCfg)

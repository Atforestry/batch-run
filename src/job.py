from datetime import datetime
import requests
import os

import logging
from logging.config import dictConfig
from log_config import log_config 

dictConfig(log_config)
logger = logging.getLogger("capstone") 

if 'FETCH_DATA_URL' in os.environ:
  FETCH_DATA_URL = os.environ['FETCH_DATA_URL']
else:
  FETCH_DATA_URL = 'NO FETCH URL'

response = requests.get('http://' + FETCH_DATA_URL + '/')

myFile = open('/usr/src/app/src/append.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()) + ' ' + str(response.status_code) + ' ' + FETCH_DATA_URL)

logger.info("Executed job.py")
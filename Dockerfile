FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get -y update    
RUN apt-get -y install cron
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src
COPY ./start.sh .

CMD ["./start.sh"]

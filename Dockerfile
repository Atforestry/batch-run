FROM python:3

ARG FETCH_DATA_URL=fetch-data:8000

ENV FETCH_DATA_URL $FETCH_DATA_URL

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get -y update    
RUN apt-get -y install cron
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src
COPY ./start.sh .

CMD ["./start.sh"]

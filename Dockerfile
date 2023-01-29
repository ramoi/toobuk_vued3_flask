FROM python:3.11.1-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/ramoi/toobuk_vued3_flask.git
WORKDIR /toobuk_vued3_flask

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD python ./toobukApp.py

# CMD flask run --app toobukApp.py -h 0.0.0.0 -p 5000
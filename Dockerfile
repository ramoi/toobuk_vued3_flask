FROM python:3.11.1-slim

CMD [ "mkdir", "toobuk_vued3_flask" ] 
WORKDIR /toobuk_vued3_flask

COPY ./ ./

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD python ./toobukApp.py

# CMD flask run --app toobukApp.py -h 0.0.0.0 -p 5000
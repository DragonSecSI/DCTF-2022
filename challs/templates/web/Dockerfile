FROM python:3.9-alpine

WORKDIR /app

COPY chall/requirements.txt /app
RUN pip install -r requirements.txt

COPY chall/server.py /app
COPY chall/shopping_list.db /app
COPY chall/templates /app/templates

EXPOSE 80
CMD python ./server.py

FROM python

WORKDIR /app

COPY server.py ./
COPY ctf.db ./

RUN pip install Flask
CMD ["python3", "server.py"]

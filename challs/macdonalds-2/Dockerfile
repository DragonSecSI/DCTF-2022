FROM ubuntu:20.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install python3 && \
    apt-get -y install python3-pip && \
    python3 -m pip install pycryptodome

COPY chall/flag.txt /
COPY chall/challenger.py /

RUN chmod 555 /challenger.py && \
    chmod 444 /flag.txt

CMD ./challenger.py

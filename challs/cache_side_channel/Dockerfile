FROM ubuntu:20.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install nano && \
    apt-get -y install libsodium-dev && \
    apt-get -y install python3 && \
    apt-get -y install python3-pip && \
    python3 -m pip install nclib

COPY chall/flag.txt /
COPY chall/app.py /
COPY chall/host /
COPY chall/libcrypto.so /
COPY chall/crypto.h /

RUN chmod 555 /app.py && \
    chmod 444 /flag.txt && \
    chmod 555 /host && \
    chmod 555 /libcrypto.so

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/

CMD ./app.py

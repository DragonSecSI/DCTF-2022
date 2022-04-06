FROM ubuntu:20.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils && \
    apt-get -y install libsodium-dev && \
    apt-get -y install python3

COPY chall/flag.txt /
COPY chall/app.py /
COPY chall/host /
COPY chall/libcrypto.so /

RUN chmod 555 /app.py && \
    chmod 444 /flag.txt && \
    chmod 555 /host && \
    chmod 555 /libcrypto.so

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/

CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 /app.py"

FROM ubuntu:20.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils python3 sagemath

COPY chall/flag.txt /
COPY chall/server.py /
COPY chall/keyfile /
COPY chall/constants.py /

RUN chmod 555 /server.py && \
    chmod 444 /flag.txt && \
    chmod 444 /constants.py && \
    chmod 444 /keyfile 

CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 python3 server.py"

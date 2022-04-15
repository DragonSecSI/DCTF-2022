FROM ubuntu:22.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils libssl-dev gcc python3


RUN mkdir /chall

COPY chall/flag.txt /chall/
COPY chall/wrapper.py /chall/
COPY chall/vm.c /chall/
COPY chall/vmstation /chall/

RUN chmod 555 /chall/vmstation && \
    chmod 444 /chall/flag.txt && \ 
    gcc /chall/vm.c -o /chall/vmstation -lcrypto -s

WORKDIR /chall
CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 /usr/bin/python3 /chall/wrapper.py"

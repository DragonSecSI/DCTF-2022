FROM ubuntu:20.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils python3

COPY chall/correcthorsebatterystaple.py /
COPY chall/wordlist.txt /

RUN chmod 555 /correcthorsebatterystaple.py && \
    chmod 444 /wordlist.txt 

CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0  python3 correcthorsebatterystaple.py"

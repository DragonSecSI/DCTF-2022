FROM ubuntu:21.10

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils qemu-system-x86 cmake gcc g++

COPY chall/serverside /serverside
COPY chall/run.py /

RUN chmod 555 /run.py

CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 python3 /run.py"

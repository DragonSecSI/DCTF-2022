FROM ubuntu:21.10

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils

COPY chall/EasyTPM_private /

RUN chmod 555 /EasyTPM_private

CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 /EasyTPM_private"

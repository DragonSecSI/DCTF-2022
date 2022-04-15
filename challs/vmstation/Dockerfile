FROM ubuntu:22.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils libssl-dev gcc python3


COPY chall/we_kind_thought_leaking_this_was_gonna_be_another_chall_flag.txt /
COPY chall/wrapper.py /
COPY chall/vm.c /

RUN gcc /vm.c -o /vmstation -lcrypto -s && \
    chmod 555 /vmstation && \
    chmod 444 /we_kind_thought_leaking_this_was_gonna_be_another_chall_flag.txt 

RUN rm /vm.c

WORKDIR /
CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 /usr/bin/python3 /wrapper.py"

FROM ubuntu:20.04

WORKDIR /app

COPY lolcode-web /app

RUN apt update -y && \
    DEBIAN_FRONTEND=noninteractive apt install git python3-pip python3 libreadline-dev make cmake -y && \
    apt-get clean && \
    git clone https://github.com/justinmeza/lci.git /lci && \
    cd /lci && \
    git checkout future && \
    cmake . && \
    make && \
    mkdir -p /app && \
    cp lci /app/lci && \
    rm -rf /lci && \
    cd /app && \
    pip3 install -r /app/requirements.txt

EXPOSE 8000
CMD [ "python3", "./server.py" ]

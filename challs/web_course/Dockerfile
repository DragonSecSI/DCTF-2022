FROM node

WORKDIR /app
ENV DB=

COPY source /app
RUN npm install && \
    apt update && \
    apt install -y netcat

EXPOSE 8000
CMD ./wait-for.sh "${DB}:27017" -- npm run start

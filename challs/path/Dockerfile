FROM node:17-alpine
ENV NODE_ENV=production

WORKDIR /app/web

COPY chall/package*.json /app/web/
RUN npm install

COPY chall/web/* /app/web/
COPY chall/flag.txt /app
COPY Dockerfile /app

EXPOSE 8000
CMD node main.js

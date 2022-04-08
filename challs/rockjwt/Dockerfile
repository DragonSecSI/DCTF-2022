FROM node:17-alpine
ENV NODE_ENV=production
ENV SECRET=light_dragon123

WORKDIR /app

COPY chall/package*.json /app/
RUN npm install

COPY chall/main.js /app
COPY chall/flag.txt /app

EXPOSE 8000
CMD node main.js

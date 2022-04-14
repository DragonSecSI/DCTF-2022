FROM node:17.0-alpine

WORKDIR /app

COPY package*.json .
RUN npm install

COPY src src

EXPOSE 8000

CMD ["npm", "run","start"]

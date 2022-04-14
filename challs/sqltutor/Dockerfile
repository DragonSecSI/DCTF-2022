FROM node:17.0-alpine

WORKDIR /usr/src/app

COPY package*.json .
RUN npm install

COPY ./src ./usr/src/app/src

EXPOSE 80

CMD ["npm", "run","start"]

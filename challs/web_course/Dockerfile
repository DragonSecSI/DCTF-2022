FROM node

WORKDIR /app

COPY source /app
RUN npm install

EXPOSE 80
CMD ./wait-for.sh ${DB} -- npm run start
FROM node:14.3.0-alpine

ADD . /app
WORKDIR /app

RUN npm install
RUN npm install -g @vue/cli

ENV CHOKIDAR_USEPOLLING=true

CMD ["npm", "run", "serve", "--", "--port"," 8080", "--host", "0.0.0.0"]

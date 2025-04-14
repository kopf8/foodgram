# build env
FROM node:23.11.0-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install -g npm@11.3.0
COPY . ./
RUN npm run build
CMD cp -r build result_build

FROM node:20-alpine

WORKDIR /app

COPY package-lock.json package.json jsconfig.json /app/

RUN --mount=type=cache,target=/root/.npm npm ci

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]
FROM node:20-alpine as builder

WORKDIR /app

COPY package-lock.json package.json jsconfig.json /app/

RUN --mount=type=cache,target=/root/.npm npm ci

COPY . .


RUN npm run build

FROM nginx:stable-alpine

COPY --from=builder /dist /usr/share/nginx/html

EXPOSE 8080

COPY --from=builder nginx.conf /etc/nginx/conf.d/default.conf

CMD [ "nginx", "-g", "daemon off;" ]
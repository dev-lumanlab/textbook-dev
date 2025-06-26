FROM nginx:latest

WORKDIR /app

RUN rm /etc/nginx/conf.d/default.conf

COPY ./dev.conf /etc/nginx/conf.d

EXPOSE 80

COPY . .

CMD ["nginx", "-g", "daemon off;"]
FROM node:20

WORKDIR /app

COPY ./iacapap_textbook_frontend/package.json ./
COPY ./iacapap_textbook_frontend/package-lock.json ./
RUN npm install

COPY ./iacapap_textbook_frontend .
RUN npm run build

EXPOSE 3000

CMD ["node", "build/index.js"]

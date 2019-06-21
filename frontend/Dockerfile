FROM node:12.4-alpine

# RUN apk --update add git openssh && \
#     rm -rf /var/lib/apt/lists/* && \
#     rm /var/cache/apk/*

WORKDIR /srv/app

COPY package.json package-lock.json ./
RUN npm install && npm cache clean --force

COPY . .
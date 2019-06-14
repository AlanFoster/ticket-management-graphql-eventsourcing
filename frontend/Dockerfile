FROM node:12.4-alpine

# RUN apk --update add git openssh && \
#     rm -rf /var/lib/apt/lists/* && \
#     rm /var/cache/apk/*

WORKDIR /srv/app

COPY package.json yarn.lock ./
RUN yarn && yarn cache clean

COPY . .
FROM node:16-alpine

WORKDIR /srv

COPY ./srv/mobydick/ /srv
RUN rm -r node_modules && npm install
CMD ["npm", "run", "dev", "--", "--host"]
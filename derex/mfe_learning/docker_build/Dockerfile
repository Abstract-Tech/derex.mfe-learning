ARG NODE_VERSION
FROM node:${NODE_VERSION} AS base

RUN apk add --no-cache \
    git \
    autoconf \
    automake \
    build-base \
    libpng-dev \
    pngquant

RUN mkdir -p /openedx/microfrontend
WORKDIR /openedx/microfrontend
ENV PATH ./node_modules/.bin:${PATH}

FROM base AS sourceonly
ARG MFE_REPOSITORY
ARG MFE_BRANCH
RUN git clone ${MFE_REPOSITORY} \
    --branch ${MFE_BRANCH} --depth 1 /openedx/microfrontend
RUN npm install
COPY .env.derex .env
RUN npm run build

FROM docker.io/caddy:2.3.0-alpine AS final

RUN mkdir -p /openedx/dist
COPY --from=sourceonly \
    /openedx/microfrontend/dist /srv/microfrontend

COPY ./Caddyfile /etc/caddy/Caddyfile

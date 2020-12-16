FROM python:3.8-buster as hind-base

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
                       build-essential \
                       git \
                       libpq-dev \
                       libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# PostgreSQL client
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
ENV PG_MAJOR 12
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main' $PG_MAJOR > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client-$PG_MAJOR \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

RUN mkdir /code/hind
WORKDIR /code/hind

COPY requirements.txt /code/hind/
RUN pip3 install --no-cache-dir -r requirements.txt
RUN useradd --create-home --shell /bin/bash hind

RUN mkdir /static
WORKDIR /static

# # Compile static files
# RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
#     apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*
# COPY package.json package-lock.json webpack.config.js tsconfig.json ./hind/webserver/static /static/
# RUN npm install && npm run build:prod && ./node_modules/less/bin/lessc --clean-css /static/css/main.less > /static/css/main.css && \
#     rm -rf node_modules js/*.jsx *.json webpack.config.js && npm cache clean --force

# Now install our code, which may change frequently
COPY . /code/hind/

WORKDIR /code/hind
RUN rm -rf ./hind/webserver/static/

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
ENV PG_MAJOR 13
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main' $PG_MAJOR > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client-$PG_MAJOR \
    && rm -rf /var/lib/apt/lists/*


# While WORKDIR will create a directory if it doesn't already exist, we do it explicitly here
# so that we know what user it is created as: https://github.com/moby/moby/issues/36677
RUN mkdir -p /code/hind /static

WORKDIR /code/hind

COPY requirements.txt requirements_development.txt /code/hind/
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements_development.txt
RUN useradd --create-home --shell /bin/bash hind

WORKDIR /static

# Install NodeJS and front-end dependencies
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*
WORKDIR /static
COPY package.json package-lock.json /static/
RUN npm install

# Compile front-end (static) files
COPY webpack.config.js babel.config.js .eslintrc.js tsconfig.json ./hind/webserver/static /static/
RUN npm run build:prod

# Now install our code, which may change frequently
COPY . /code/hind/

WORKDIR /code/hind
RUN rm -rf ./hind/webserver/static/

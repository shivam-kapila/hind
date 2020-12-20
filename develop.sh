#!/bin/bash

POSTGRES_HIND_URI="postgresql://hind:hind@db/hind"

if [[ ! -d "docker" ]]; then
    echo "This script must be run from the top level directory of the hind-server source."
    exit -1
fi

function invoke_docker_compose {
    exec docker-compose -f docker/docker-compose.yml \
                -p hind \
                "$@"
}

function invoke_manage {
    invoke_docker_compose run --rm web \
            python3 manage.py \
            "$@"
}

function open_psql_shell {
    invoke_docker_compose run --rm web psql \
        ${POSTGRES_HIND_URI}
}

function open_bash_shell {
    invoke_docker_compose run --rm web bash
}

function lint_frontend_code {
    invoke_docker_compose run --rm static_builder \
               npm run format
}

# Arguments following "manage" are passed to manage.py inside a new web container.
if [[ "$1" == "manage" ]]; then shift
    echo "Running manage.py..."
    invoke_manage "$@"

elif [[ "$1" == "bash" ]]; then
    echo "Running bash..."
    open_bash_shell

elif [[ "$1" == "psql" ]]; then
    echo "Connecting to postgresql..."
    open_psql_shell

elif [[ "$1" == "lint" ]]; then
    echo "Linting frontend code..."
    lint_frontend_code

else
    echo "Running docker-compose with the given command..."
    invoke_docker_compose "$@"
fi

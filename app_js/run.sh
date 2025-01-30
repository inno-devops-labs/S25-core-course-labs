#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
IMAGE_NAME="s25-devops-cryptoclicker"

source ./.env

if [ "$DOCKER_NO_SAVE" == 1 ]; then
    docker image rmi "$IMAGE_NAME" > /dev/null;
fi
if [[ -z $(docker images | grep -w "$IMAGE_NAME") ]]; then
    docker build -t "$IMAGE_NAME" "$SCRIPT_DIR";
fi

if [[ -z $(docker ps -a | grep -w "${IMAGE_NAME}_ct") ]]; then
    docker run -i \
        $([ "$DOCKER_NO_SAVE" == 1 ] && echo "--rm") \
        $([ "$DEV" == 1 ] && 
            echo "--mount type=bind,src=$SCRIPT_DIR/src,dst=/app/src";
            echo "--mount type=bind,src=$SCRIPT_DIR/public,dst=/app/public";
        ) \
        --env-file .env \
        -p "$APP_PORT:$APP_PORT" \
        --name "${IMAGE_NAME}_ct" \
        "$IMAGE_NAME";
else
    docker start -a "${IMAGE_NAME}_ct";
fi

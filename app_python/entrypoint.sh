#!/bin/bash

_term() { 
  kill -INT "$child" 2>/dev/null
}

trap _term SIGINT

uvicorn \
    $([ "$DEV" == 1 ] && 
      echo "--reload";
    ) \
    src.main:app \
    --workers 1 \
    --host "$APP_HOST" \
    --port "$APP_PORT" \
    &

child=$!
wait "$child"

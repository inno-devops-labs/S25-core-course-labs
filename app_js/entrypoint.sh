#!/bin/bash

_term() { 
  kill -INT "$child" 2>/dev/null
}

trap _term SIGINT
trap _term SIGTERM

npm run \
  $([ "$DEV" == 1 ] && 
      echo "dev" || echo "preview"
  ) -- \
  --host "$APP_HOST" \
  --port "$APP_PORT" \
  &

child=$!
wait "$child"

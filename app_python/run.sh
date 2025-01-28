#!/bin/bash

APP_ADDRESS="127.0.0.1"
APP_PORT=8000

HOT_RELOAD=1

uvicorn $([ "$HOT_RELOAD" == 1 ] && echo "--reload") src.main:app \
    --workers 1 \
    --host "$APP_ADDRESS" \
    --port "$APP_PORT"

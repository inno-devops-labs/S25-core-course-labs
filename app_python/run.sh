#!/bin/bash

# Change the port if busy
uvicorn app.main:app --reload --host 0.0.0.0 --port 8081


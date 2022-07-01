#!/usr/bin/env bash

rm -f celerybeat.pid
celery "$@"

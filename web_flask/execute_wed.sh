#!/usr/bin/env bash
# ejecuta la web_Flask
kill -9 $(ps -A | grep python | awk '{print $1}')
export FLASK_APP=$1
python3 -m flask run --host=0.0.0.0

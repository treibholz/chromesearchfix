#!/bin/sh
export FLASK_APP=search.py
cd $(dirname ${0})
flask run -p 10080 $@
cd -

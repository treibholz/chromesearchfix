#!/bin/sh
export FLASK_APP=search.py
flask run -p 10080 $@

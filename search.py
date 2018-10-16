#!/usr/bin/python3

from flask import Flask, request, redirect
from urllib.parse import urlparse
from socket import gethostbyname
from re import match

app = Flask(__name__)

def str2bool(value):
    return value.lower() in ( "true", "1", "yes")

@app.route("/")
def index():
    return "nothing to see here!"

@app.route('/search', methods=['GET'])
def search():
    searchword      = request.args.get('q', '')
    protect         = request.args.get('protect', 'dev')
    engine          = request.args.get('engine', 'https://duckduckgo.com/?q=%s')
    default_scheme  = request.args.get('default_scheme', 'http')
    _resolv        = request.args.get('resolv', 'true')

    resolv = str2bool(_resolv)
    _match  = '.*\.(%s)(\.)?$' % (protect,)

    o = urlparse(searchword)
    if o.netloc=='':
        o = urlparse('%s://%s' % (default_scheme, searchword,) )

    try:
        if resolv:
            dns_result = gethostbyname(o.hostname)
            target_url = o.geturl()
            print("I can resolv %s: %s!" % (o.hostname, dns_result,))
        else:
            raise ValueError('resolv is set to False')
    except:
        if match(_match, o.hostname):
            print(_match)
            target_url=o.geturl()
        else:
            print(engine)
            target_url = engine % searchword

    return redirect(target_url)

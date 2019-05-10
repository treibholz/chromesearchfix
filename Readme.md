# chromesearchfix

This is a pseudo-search-engine to use in google-chrome or chromium, to prevent
searching for internal hostnames or FQDNSs online.

## Why do you need this?

e.g. if you write "webserver01" in your addressbar, chrome will search for it
in the defaut-searchengine, instead of browsing to "http://webserver01"

Even if you write "webserserver01.internal.dev", chrome will do this.

Chromesearchfix will help to prevent this, by trying to resolve "webserver01",
if it can be resolved, it redirects you to "https://webserver01".

If the "searchword" can't be resolved, you get redirected to a search-engine
with a search for "searchword". Except if the "searchword" ends with a domain
(e.g. dev), you want to protect, then you will always be redirected to
https://$searchword (e.g. https://webserver01.internal.dev)

# Usage

```
$ FLASK_APP=search.py flask run -p 10080
 * Serving Flask app "search"
 * Running on http://127.0.0.1:10080/ (Press CTRL+C to quit)
```

add the following URL to your search-Engines:

    http://localhost:10080/search?q=%s

## Configuration

The config-options can be set in the URL:

#### protect

the default_scheme you want to use, separated by |. default=dev

Example:

    http://localhost:10080/search?q=%s&protect=lan|dev|qa

#### engine

the search-engine you want to use. default=https://duckduckgo.com/?q=%s
Use urlencode!

Example:

    http://localhost:10080/search?q=%s&engine=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3D%25s

#### default_scheme

the default_scheme you want to use, default=https

Example:

    http://localhost:10080/search?q=%s&default_scheme=http

#### resolv

Set this to false, if you don't want to try to resolve it. default=true

Example:

    http://localhost:10080/search?q=%s&resolv=false

## use systemd

    # ./enable_user_systemd.sh
    Created symlink /home/YOUR_USERNAME/.config/systemd/user/basic.target.wants/chromesearchfix.service → /home/YOUR_USERNAME/.config/systemd/user/chromesearchfix.service.
    ● chromesearchfix.service - ChromeSearchFix
        Loaded: loaded (/home/YOUR_USERNAME/.config/systemd/user/chromesearchfix.service; enabled; vendor preset: enabled)
        Active: active (running) since Fri 2019-05-10 16:15:35 CEST; 3ms ago
     Main PID: 19675 (run.sh)
       CGroup: /user.slice/user-1000.slice/user@1000.service/chromesearchfix.service
               ├─19675 /bin/sh /home/YOUR_USERNAME/git/chromesearchfix/run.sh
               └─19678 /usr/bin/python3 /usr/bin/flask run -p 10080


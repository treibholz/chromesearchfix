# chromesearchfix

## Usage

```sh
$ FLASK_APP=search.py flask run -p 10080
 * Serving Flask app "search"
 * Running on http://127.0.0.1:10080/ (Press CTRL+C to quit)
```

add the following URL to your search-Engines:

    http://localhost:10080/search?q=%s

you may add more options:

### protect

protects the domains, you want to protect as part of a regex, default: protect=lan

Example:

    http://localhost:10080/search?q=%s&protect=lan|dev|qa

### engine

the search-engine you want to use. default=https://duckduckgo.com/?q=%s
Use urlencode!

Example:

    http://localhost:10080/search?q=%s&engine=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3D%25s

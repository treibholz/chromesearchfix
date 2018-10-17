FROM alpine:3.8

ENV FLASK_APP search.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apk add --no-cache py3-flask
COPY $FLASK_APP /
USER nobody
EXPOSE 10080

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "10080", "--with-threads"]

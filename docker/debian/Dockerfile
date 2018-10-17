FROM debian:stretch-slim

ENV FLASK_APP search.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-flask python3-pkg-resources && \
    apt-get clean && \
    apt-get -yq autoremove && \
    rm -rf /var/lib/apt/lists/*

COPY $FLASK_APP /
USER nobody
EXPOSE 10080

CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "10080", "--with-threads"]

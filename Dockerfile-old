FROM alpine:3.10

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3 python3-dev gcc musl-dev &&\
    pip3 install flask fuzzywuzzy[speedup]

EXPOSE 80

WORKDIR /code

ADD app.py excuses.txt ./

EXPOSE 80

CMD ["python3", "app.py"]

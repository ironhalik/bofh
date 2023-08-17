FROM python:3.11-alpine3.18

RUN pip3 install flask fuzzywuzzy[speedup]

ENV PYTHONUNBUFFERED=1

EXPOSE 80

WORKDIR /code

ADD app.py excuses.txt ./

EXPOSE 80

CMD ["python3", "app.py"]
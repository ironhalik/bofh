from flask import Flask, json, Response, request
from random import choice
from fuzzywuzzy import fuzz, process
from os import getenv

app = Flask(__name__)

excuses = []
with open("excuses.txt") as file:
    for line in file:
        excuses.append(line.strip('\n'))

@app.route('/bofh', methods = ['GET', 'POST'])
def bofh():
    if "text" in request.form and request.form["text"]:
        quotes = process.extract(request.form["text"], excuses, limit=5)
        quote = choice(quotes)[0]
    else:
        quote = choice(excuses)

    response = json.dumps({"response_type": "in_channel", "text": quote})
    return Response(response, mimetype="application/json")

if __name__ == '__main__':
    app.run('0.0.0.0', int(getenv("PORT","80")))
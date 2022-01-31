from csv import DictReader
from flask import current_app as app, request, abort
from flask.json import dumps
import requests

@app.route("/api/resume/<string:name>", methods=["GET"])
def get_resume(name: str):
    FILE_NAME = "test.csv"

    url = request.args.get("url", type=str)

    if url:
        try:
            with requests.Session() as session:
                stream = session.get(url)
                file = stream.content.decode("utf-8")
                reader = DictReader(file)
                json = dumps([row for row in reader], indent=4)
                return json

        except Exception as e:
            print(e.args)
            return abort(500)

    with open(FILE_NAME, encoding="utf-8") as file:
        reader = DictReader(file)
        json = dumps([row for row in reader], indent=4)
        return json
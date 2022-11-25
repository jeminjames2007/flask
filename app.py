from flask import Flask
from flask import request
app = Flask(__name__)

store = [
    {"name":"Store1","location":"Location1"},
    {"name":"Store2","location":"Location2"}
]

@app.get("/")
def get_data():
    return {"stores":store}

@app.post("/")
def create():
    request_data = request.get_json()
    new_val = {"name":request_data["name"], "location":request_data["location"]}
    store.append(new_val)
    return new_val
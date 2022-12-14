from flask import Flask
from flask import request
from db import stores,items
import uuid
from flask_smorest import abort
app = Flask(__name__)

@app.get("/")
def get_all_stores():
    return {"stores":list(stores.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message = "Store not found")

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    if("name" not in store_data or "price" not in store_data):
        abort(400,message = "Please check required fields")
    
    new_store = {**store_data,"id":store_id}
    stores[store_id] = new_store
    return new_store,200

@app.get("/item")
def get_all_items():
    return {"items":list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message = "Item not found")

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message":"Store not found"},404
    item_id = uuid.uuid4().hex
    item = {**item_data,"id":item_id}
    item[item_id] = item
    return item,200




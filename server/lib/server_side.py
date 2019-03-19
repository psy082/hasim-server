# -- coding: utf-8 --

from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "users"
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/users"

mongo = PyMongo(app)

@app.route("/login", methods=["POST"])
def login(userid):
    users = mongo.db.users 
    existing_user = users.find_one({"id" : userid})

    if existing_user is None:
        users.insert({"id" : userid})
        return "You are registed now!"
    return "You are already our member!"

@app.route("/register", method=["POST"])
def register():
    users = mongo.db.users
    existing_user = users.find_one({"id" : userid})

    if existing_user is None:
        users.insert({"id": userid})
        return "등록되었습니다!"
    return "이미 등록된 회원입니다" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


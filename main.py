from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient

from bson import ObjectId

# Instantiation
app = Flask(__name__)
app.config['SECRET_KEY'] = '43386720cb87a1463f0f41c2ac6d47865ded43d5'
app.config['MONGO_URI'] = 'mongodb+srv://albert:162003@cluster0.ned4xp7.mongodb.net/?retryWrites=true&w=majority'

connect = MongoClient(app.config['MONGO_URI'])

db = connect['khkt_db']['khkt_tables']


@app.route('/')
def home():
    return "hello"


@app.route('/msg', methods=['GET', 'POST'])
def msg():
    if request.method == 'POST':
        data = request.json.get('data')
        db.insert_many(data)
    else:
        print("get")
    return "request.body"


if __name__ == "__main__":
    app.run(debug=True)

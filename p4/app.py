from flask import Flask, logging, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Set your MongoDB URI here directly or retrieve it from environment variables
# Replace 'your_username', 'your_password', and 'your_database' with your actual credentials
mongo_uri = 'mongodb+srv://cancer:E8KvBWc3hTacvWPZ@cluster0.tui45c4.mongodb.net/'

# app.config["MONGO_URI"] = mongo_uri
mongo = MongoClient(mongo_uri)
# print(mongo.list_database_names())

# Define endpoint to render the HTML template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2.html')
def index2():
    return render_template('index2.html')

@app.route('/index3.html')
def index3():
    return render_template('index3.html')

@app.route('/index4.html')
def index4():
    return render_template('index4.html')

# Define endpoint to fetch data from MongoDB and return as JSON

@app.route('/diesel')
def getGAS1():
    db = mongo["GAS"]
    data = db["Diesel"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

@app.route('/reg_gas')
def getGAS2():
    db = mongo["GAS"]
    data = db["Reg_gas"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

@app.route('/pre_gas')
def getGAS3():
    db = mongo["GAS"]
    data = db["Pre_gas"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

@app.route('/heat')
def getGAS4():
    db = mongo["GAS"]
    data = db["Heat"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

@app.route('/cpi')
def getCPI():
    db = mongo["CPI"]
    data = db["CPI"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

@app.route('/pop')
def getPop():
    db = mongo["Pop"]
    data = db["Pop"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

@app.route('/emp')
def getEmp():
    db = mongo["Employment"]
    data = db["Employ"]
    documents = list(data.find({}, {'_id': 0}))  # Excludes the _id field
    return jsonify(documents)

if __name__ == '__main__':
    app.run(debug=True)
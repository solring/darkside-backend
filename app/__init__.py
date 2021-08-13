from flask import Flask, request, jsonify
#from pymongo import MongoClient

app = Flask(__name__)

mockData = [
    {"mock": 123456}
]

@app.route("/article/<category>", methods=['POST'])
def getArticlesByCategory(category):
    print("get category %s" % category)
    data = request.get_json()

    start, length = data['start'], data['length']

    if start >= len(mockData):
        return {}

    end = min(start+length, len(mockData))

    data = mockData[start:end]

    return jsonify(data)

@app.route("/echo")
def echoTest():
    return "Hello!"

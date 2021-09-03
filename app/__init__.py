from os import environ
from flask import Flask, request, jsonify
from flask_cors import CORS
from .queries import DBQuery
from .log import log

url = environ.get('MONGO_URL')

MONGODB = "%s:27017" % url if url else "127.0.0.1:27017"
DB = "darkside"
COLLECTION = "articles"
dbq = DBQuery(MONGODB, DB, COLLECTION)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def pack(result, nxt):
    d = {}
    for r in result:
        for t in r['tags']:
            d[t] = 1
    tags = [ k for k in d.keys() ]

    obj = {
        'data': {
            'list': result,
            'next': nxt,
            'tags': tags
        }
    }
    return jsonify(obj)

@app.route("/api/article/", methods=['POST'])
def get_article_all():

    data = request.get_json()
    start = data['start'] if 'start' in data else 0
    length = data['length'] if 'length' in data else 0
    log(get_article_all, "start: %d, len: %d." %(start, length))

    res, nxt = dbq.get_all(start, length)
    return pack(res, nxt)

@app.route("/api/article/<category>", methods=['POST'])
def get_article_by_category(category):

    log(get_article_by_category, "get category: %s" % category)

    data = request.get_json()

    start = data['start'] if 'start' in data else 0
    length = data['length'] if 'length' in data else 0
    log(get_article_by_category, "start: %d, len: %d." %(start, length))

    res, nxt = dbq.get_by_category(category, start, length)
    return pack(res, nxt)

@app.route("/api/tag/all", methods=['GET'])
def get_tags_all():
    res = dbq.get_total_tags()
    log(get_tags_all, res)
    return jsonify(res)

@app.route("/api/tag/<category>", methods=['GET'])
def get_tags_by_category(category):
    res = dbq.get_category_tags(category)
    log(get_tags_all, res)
    return jsonify(res)

@app.route("/echo")
def echoTest():
    return "Hello!"

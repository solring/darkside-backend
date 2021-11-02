from os import environ
from flask import Flask, request, jsonify
from flask_cors import CORS
from .queries import DBQuery
from .log import log

url = environ.get('MONGO_URL')
user = environ.get('MONGO_USER')
pwd = environ.get('MONGO_PWD')

MONGODB = "%s:27017" % url if url else "127.0.0.1:27017"
DB = "darkside"
COLLECTION = "articles"
dbq = DBQuery(MONGODB, user, pwd, DB, COLLECTION)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def pack(result, nxt, cat=""):
    d = {}
    for r in result:
        for t in r['tags']:
            d[t] = 1
    tags = [ k for k in d.keys() ]

    obj = {
        'data': {
            'list': result,
            'next': nxt,
            'category': cat,
            'tags': tags
        }
    }
    return jsonify(obj)

@app.route("/api/articles/", methods=['GET'])
def get_article_all():
    start = int(request.args.get('start')) if request.args.get('start') else 0
    length = int(request.args.get('length')) if request.args.get('length') else 0
    log(get_article_all, "start: %d, len: %d." %(start, length))

    res, nxt = dbq.get_all(start, length)
    return pack(res, nxt)

@app.route("/api/articles/<category>", methods=['GET'])
def get_article_by_category(category):

    log(get_article_by_category, "get category: %s" % category)

    start = int(request.args.get('start')) if request.args.get('start') else 0
    length = int(request.args.get('length')) if request.args.get('length') else 0
    log(get_article_by_category, "start: %d, len: %d." %(start, length))

    res, nxt = dbq.get_by_category(category, start, length)
    return pack(res, nxt, cat=category)

@app.route("/api/tags/", methods=['GET'])
def get_tags_all():
    res = dbq.get_total_tags()
    log(get_tags_all, res)
    return jsonify(res)

@app.route("/api/tags/<category>", methods=['GET'])
def get_tags_by_category(category):
    res = dbq.get_category_tags(category)
    log(get_tags_all, res)
    return jsonify(res)

@app.route("/api/categories/", methods=['GET'])
def get_category_all():
    res = dbq.get_total_category()
    log(get_category_all, res)
    return jsonify(res)

@app.route("/api/article", methods=['POST'])
def create_article():
    data = request.get_json()
    log(create_article, ": insert article")
    dbq.insert_article(
        title = data["title"] if "title" in data else "",
        img_url = data["img"] if "img" in data else "",
        desc = data["desc"] if "desc" in data else "",
        category = data["category"] if "category" in data else "",
        tags = data["tags"] if "tags" in data else "",
    )

    return jsonify({ 'ok': True })

# FOR TESTING
@app.route("/echo")
def echoTest():
    return "Hello!"

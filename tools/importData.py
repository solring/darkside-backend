from pymongo import MongoClient
from sys import argv
from csv import DictReader
import re

DB = "darkside"
COLLECTION = "articles"

if __name__ == "__main__":
    if len(argv) < 5:
        print("[usage]: python %s [csv file to import] [host] [user] [pwd]" % argv[0])
        exit(0)

    filename, host, user, pwd = argv[1:]

    client = MongoClient(host,
        username=user, password=pwd, authSource='admin', authMechanism='SCRAM-SHA-256')
    db = client[DB]
    article = db[COLLECTION]

    with open(filename, 'r') as fd:
        data = DictReader(fd)

        data = [ r for r in data ]
        for i in range(len(data)):
            data[i]["height"] = float(data[i]["height"])
            data[i]["tags"] = [ data[i]["tags"] ]
            data[i]["id"] = i

        res = article.insert_many(data)
        print(res.inserted_ids)


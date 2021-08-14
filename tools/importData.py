from pymongo import MongoClient
from sys import argv
from csv import DictReader
import re

# mongo db location
MONGODB = "mongodb://localhost:27017/"
DB = "darkside"
COLLECTION = "articles"

if __name__ == "__main__":
    if len(argv) < 2:
        print("[usage]: python %s [csv file to import]")
        exit(0)

    client = MongoClient(MONGODB)
    db = client[DB]
    article = db[COLLECTION]

    filename = argv[1]
    with open(filename, 'r') as fd:
        data = DictReader(fd)

        data = [ r for r in data ]
        for i in range(len(data)):
            data[i]["height"] = float(data[i]["height"])
            data[i]["tags"] = [ data[i]["tags"] ]
            data[i]["id"] = i

        res = article.insert_many(data)
        print(res.inserted_ids)


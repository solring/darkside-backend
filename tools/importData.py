from pymongo import MongoClient
from sys import argv
from csv import DictReader
import re

# mongo db location
MONGODB = "mongodb://localhost:27017/"
COLLECTION = "articles"
IMG = "img"

if __name__ == "__main__":
    if len(argv) < 2:
        print("[usage]: python %s [csv file to import]")
        exit(0)

    client = MongoClient(MONGODB)
    db = client.darkside
    article = db[COLLECTION]

    filename = argv[1]
    with open(filename, 'r') as fd:
        data = DictReader(fd)

        data = [ r for r in data ]

        res = article.insert_many(data)
        print(res.inserted_ids)


from pymongo import MongoClient

def_proj = {'_id': False}

class DBQuery:

    def __init__(self, entrypoint, db_name, collection):
        self.client = MongoClient(entrypoint)
        self.db = self.client[db_name]
        self.col = self.db[collection]

    def get_all(self, start, length):
        res = [ i for i in self.col.find({}, skip=start, limit=length, projection=def_proj)]

        return (res, start+len(res))

    def get_by_category(self, category, start, length):
        res = [ i for i in self.col.find({'category': category}, skip=start, limit=length, projection=def_proj)]

        return (res, start+len(res))

    def get_total_tags(self):
        pipeline = [
            { '$unwind': '$tags' },
            {
                '$group': {
                    '_id': '$tags',
                    'count': { '$sum' : 1 }
                }
            },
        ]

        res = self.col.aggregate(pipeline)
        return [ r['_id'] for r in res ] if res else []

    def get_category_tags(self, category):
        pipeline = [
            { '$match': { 'category' : category } },
            { '$unwind': '$tags' },
            {
                '$group': {
                    '_id': '$tags',
                    'count': { '$sum' : 1 }
                }
            },
        ]

        res = self.col.aggregate(pipeline)
        return [ r['_id'] for r in res ] if res else []

    def get_by_tags(self, tags, start, end):
        if not tags:
            return self.get_all(start, end)

        res = [ i for i in self.col.find({'tags': {'$in': tags}}, projection=def_proj) ]
        return res[start:end]


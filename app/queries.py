from pymongo import MongoClient

defProj = {'_id': False}

class DBQuery:

    def __init__(self, entrypoint, db_name, collection):
        self.client = MongoClient(entrypoint)
        self.db = self.client[db_name]
        self.col = self.db[collection]
        self.cache = {}

    def get_result(self, cache, start, end):
        return (cache[start:end], min(end, len(cache)))

    def get_all(self, start, end):
        print("get all: %d, %d." %(start, end))
        if 'all' not in self.cache:
            self.cache['all'] = [ i for i in self.col.find({}, projection=defProj)]

        return self.get_result(self.cache['all'], start, end)

    def get_by_category(self, category, start, end):
        print("get by cate: %d, %d." %(start, end))
        if category not in self.cache:
            self.cache[category] = [ i for i in self.col.find({'category': category}, projection=defProj)]

        return self.get_result(self.cache[category], start, end)

    def get_by_tags(self, tags, start, end):
        if not tags:
            return self.get_all(start, end)

        res = [ i for i in self.col.find({'tags': {'$in': tags}}, projection=defProj) ]
        return res[start:end]

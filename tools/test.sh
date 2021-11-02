curl -X GET http://127.0.0.1:5000/echo
curl -X GET 'http://127.0.0.1:5000/api/articles/?start=5&length=5'
curl -X GET 'http://127.0.0.1:5000/api/articles/illustration?start=5&length=5'
curl -X GET 'http://127.0.0.1:5000/api/tags/'
curl -X GET 'http://127.0.0.1:5000/api/tags/illustration'
curl -X GET 'http://127.0.0.1:5000/api/categories/'
# curl -X POST -H "Content-Type: application/json" -d '{ "title": "testTitle", "desc": "this is a test", "category": "testCat" }' http://127.0.0.1:5000/api/article
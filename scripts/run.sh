MONGO_URL=localhost MONGO_PWD=darksidedb MONGO_USER=solring MONGO_PORT=27019 gunicorn -w 4 -b 127.0.0.1:5000 app:app

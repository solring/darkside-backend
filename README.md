# Getting Start

1. Install virtualenv and python 3(with pip)
2. Build virtualenv
```
virtualenv env
```
3. Activate virtualenv
```
source env/bin/activate
```
4. Install required packages
```
pip install requirements.txt
```

## Updating requirement
```
pip freeze > requirements.txt
```

# Start Server

## Start backend server with MongoDB using Docker

Requires `docker` and `docker-compose`

Currently using local volumns rather than mounted volumn.
```
./scripts/startdocker.sh
```

## Start locally (backend server only)
```
./scripts/run.sh
```

# Testing

Testing scripts using `curl` are located in `./tools/test.sh`

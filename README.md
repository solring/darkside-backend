# Getting Start

1. Install virtualenv and python 3(with pip)
2. Build virtualenv folder
```
virtualenv env
```
3. Activate virtualenv
```
source env/bin/activate
```
4. Install required packages
```
pip3 install requirement.txt
```

## Updating requirement
```
pip3 freeze > requirement.txt
```

# Start Server

## Start MongoDB using Docker
Docker is required.
Currently using local volumns rather than mounted volumn.
```
./startdocker.sh
```

## Start backend server
```
./run.sh
```

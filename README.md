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

### Use mounted volumes
1. Create folder to be mounted as docker volume and to store DB data.
2. Modify `docker-compose.env`. Change the environment variable to your created folder.
    ``` docker-compose.env
    MONGO=/path/to/your/db/folder
    ```
3. Run `startdocker.sh`
    ```
    ./scripts/startdocker.sh
    ```


### Use local volumes
This is an alternative option if your local filesystem cannot be mounted by docker(e.g. OS X or Windows).
1. Copy `docker-compose.yaml.localvolume` as `docker-compose.yaml`.
2. Run `startdocker.sh`
    ```
    ./scripts/startdocker.sh
    ```

## Start locally (backend server only)
```
./scripts/run.sh
```

# Testing

Testing scripts using `curl` are located in `./tools/test.sh`

# Importing data

Python scripts and example data for importing articles from .csv are located in `./tools/`
After starting the server, data can be imported by running the script:
```
python3 importData.py [csv you want to import]
```

# Setting Certificate for HTTPS

1. Prepare your certificate(crt + ca bundle from your CA provider, concatenated togather.) and key.
2. Create `ssh/` folder in the root of this repo.
3. Copy the certificate and the key into `ssh/` as `server.crt` and `server.key`
4. Start the server using docker-compose


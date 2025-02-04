# HexMatch

Let's match up consumers and providers on a hexagonal board


![map](./docs/hex.png)


## Setup Gcloud 

```bash
gcloud auth application-default login
make instancecreate
make loadschema
```


## Get Python setup and load the Data

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./load_data.py
```

## Start Querying

[Queries](./SampleQueries.md)

## Running Raw Queries


### Project Overview

- Create stores, each with a `name` and a list of stocked `items`.
- Create an item within a store, each with a `name` and a `price`.
- Retrieve a list of all stores and their items.
- Given its `name`, retrieve an individual store and all its items.
- Given a store `name`, retrieve only a list of item within it.


#### Create stores

Request:
```
POST /store {"name": "MyStore"}
```

Response
```
{"name": "My Store", "items": []}
```

#### Create items

Request:
```
Post /store/My Store/item {"name": "Chair", "price": 175.50}
```

Response:
```
{"name": "Chair", "price": 175.50}
```

#### Retrieve all stores and their items

Request: 
```
Get /store
```

Response:
```
{
    "stores": [
        {
            "name": "My Store",
            "items": [
                {
                    "name": "Chair",
                    "price": 175.50
                }
            ]
        }
    ]
}
```

#### Get a particular store

Request: 
```
GET /store/My Store
```

Response
```
{
    "name": "My Store",
    "items": [
        "name": "Chair",
        "price": 175.50
    ]
}
```

#### Get only items in a store

Request
```
GET /store/My Store/item
```

Response
```
[
    {
        "name": "Chair",
        "price": 175.50
    }
]
```

### Getting set up

Create a python virtual env
```
$ python -m venv .venv
```

Tell the vscode which env to use
Cmd + Shift + P
Select Interpretter
Find the path
reopen terminal

```
@thavaahariharangit ➜ /workspaces/Learning-python (main) $  source /workspaces/Learning-python/M03/Recording/.venv/bin/activate
(.venv) @thavaahariharangit ➜ /workspaces/Learning-python (main) $ 
```

Install flask
```
$ pip install flask
```

create app.py
```
from flask import Flask

app = Flask(__name__)
```

run the app
```
flask run

* Running on http://127.0.0.1:5000
```
Server started


### My First Rest API

```
from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.get('/store')
def get_stores():
    return {'stores': stores}
```

### What is JSON

Long string with specific format which can include
- Strings
- Numbers
- Booleans (`true` or `false`)
- Lists
- Objects (akin to dictionaries in python)

Top level json can be a List or objects

### How to interact with and test your REST API
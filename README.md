# py-threads-client

A Python client for [go-threads](https://github.com/textileio/go-threads).

# Installation (virtualenv)

```
$ git clone git@github.com:numbersprotocol/py-threads-client.git
$ python3 -m venv venv
$ pip3 install py-threads-client/
```

# Usage

### Import

```
from pythreads import Client
```

### Create a new client with given connection info

```
client = Client('34.204.214.19', '6006')
```

### Create a new store (if you want to start a new store)

```
store_id = client.new_store()
```

Before retrieving the store invitation link or do anything to the store, you have to initialize the client with the given store first.

If you're starting a new store, use the `store_id` you get from `new_store()`.

If you're joining a existing store, you can use the existing store id.

There are two API calls that can initiate a client, the `start()` and `start_from_address()`. Use the former for the local store (the store which is available on the Thread daemon you connected to), and use the latter for a store available on remote Thread daemon node.

### Start from local store

```
client.start(store_id)
```

### Start from remote store

```
client.start_from_address(store_id, address, follow_key, read_key)
```

### Start from invitation link

A shortcut to `start_from_address()`, parsing the invitation link for you.

```
client.start_from_link(store_id, link)
```

### Get store invitation link

To get the `address`, `follow_key` and `read_key` of a store, you can use the `get_store_link()` API.

```
links = client.get_store_link(store_id)
```

The returned value is a `list` of `str`. Each string is a invitation link which is in the format of `<address>?<follow_key>&<read_key>`.

Here is an example:

```
/ip4/127.0.0.1/tcp/4006/p2p/123458qhhfuhUDHUIGHFIoafaaffopqfpqjgpUSGUIOIfjalfjiqgnAHOIHGO/thread/qihoh122hfhwhgueheudsfq8hqHDUAHfhqqioghoqi?jqiotjorODHUQHUHohfqhfouqhohauhqogfq3jq2oriwo&hhHSUHuihquihugfeqeqhofuqhfuhqhfwufhofhqouhfq
```

You can extract the address, follow key and read key from the invitation links.

Note that there would be a couple of links in the returned list, each corresponds to an address.

Usually, some addresses are not available for you to connect (e.g. `127.0.0.1` or private addresses). You have to test it out.

### Register a schema

To register a schema, you have to provide a JSON schema string as an argument.

```
# Give the model collection a name
model_name = 'Media'

with open('examples/schemas/media.json', 'r') as f:
    schema = f.read()
try:
    resp = client.register_schema(store_id, model_name, schema)
except Exception:
    print('Schema already registered')
```

### Create a model (a data entity)

Let's say you have registered a model schema. Now it's time to add some models.

```
data1 = {
    'dataHash': 'ccccggggcdecdddd116bbb2bb2ccccccf8339dddddf9eeeeeb41578a44',
    'metadataHash': 'ccccccggg_1bbbeeeee6'    
}

resp = client.model_create(store_id, model_name, [data1])
```

### Find all models

```
entities = client.model_find(store_id, model_name)
```

### Find, modify and save a model

```
entity = client.model_find_by_id(store_id, model_name, entity_id)
entity['dataHash'] = 'blablabla'
resp = client.model_save(store_id, model_name, [entity])
```

### Check if models exist

```
entity_ids = [entity1['ID'], entity2['ID'], entity3['ID']]
if client.model_has(store_id, model_name, entity_ids):
    print('Models found!')
```

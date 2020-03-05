import json
import uuid

import base58
import grpc

from pythreads.api import api_pb2
from pythreads.api import api_pb2_grpc
from pythreads.config import Config


class Client():
    def __init__(self, host='127.0.0.1', port='6006'):
        self.config = Config(host, port)
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.config.host, self.config.port)
        )
        self.stub = api_pb2_grpc.APIStub(self.channel)

    def new_store(self) -> str:
        req = api_pb2.NewStoreRequest()
        resp = self.stub.NewStore(req)
        if not resp.ID:
            raise KeyError('ID not found in new_store response')
        return resp.ID

    def register_schema(self, store_id, model_name, schema):
        req = api_pb2.RegisterSchemaRequest(
            storeID=store_id,
            name=model_name,
            schema=schema,
        )
        resp = self.stub.RegisterSchema(req)
        return resp

    def start(self, store_id):
        req = api_pb2.StartRequest(storeID=store_id)
        self.stub.Start(req)
        return

    def start_from_address(self, store_id, address, follow_key, read_key):
        req = api_pb2.StartFromAddressRequest(
            storeID=store_id,
            address=address,
            followKey=base58.b58decode(follow_key),
            readKey=base58.b58decode(read_key),
        )
        resp = self.stub.StartFromAddress(req)
        return resp

    def start_from_link(self, store_id, invite_link):
        address = invite_link.split('?')[0]
        follow_key = invite_link.split('?')[1].split('&')[0]
        read_key = invite_link.split('&')[1]
        self.start_from_address(store_id, address, follow_key, read_key)

    def get_store_link(self, store_id):
        req = api_pb2.GetStoreLinkRequest(storeID=store_id)
        resp = self.stub.GetStoreLink(req)
        addresses = resp.addresses
        follow_key = str(base58.b58encode(resp.followKey), 'utf-8')
        read_key = str(base58.b58encode(resp.readKey), 'utf-8')
        return [
            '{}?{}&{}'.format(
                address, follow_key, read_key
            ) for address in addresses
        ]

    def model_create(self, store_id, model_name, values=[]):
        values_json = []
        for v in values:
            v['ID'] = str(uuid.uuid4())
            values_json.append(json.dumps(v))
        req = api_pb2.ModelCreateRequest(
            storeID=store_id,
            modelName=model_name,
            values=values_json,
        )
        resp = self.stub.ModelCreate(req)
        return [json.loads(e) for e in resp.entities]

    def model_save(self, store_id, model_name, values=[]):
        values_json = [json.dumps(v) for v in values]
        req = api_pb2.ModelSaveRequest(
            storeID=store_id,
            modelName=model_name,
            values=values_json,
        )
        resp = self.stub.ModelSave(req)
        return resp

    def model_delete(self, store_id, model_name, entity_ids=[]):
        req = api_pb2.ModelDeleteRequest(
            storeID=store_id,
            modelName=model_name,
            entityIDs=entity_ids,
        )
        resp = self.stub.ModelDelete(req)
        return resp

    def model_has(self, store_id, model_name, entity_ids=[]) -> bool:
        req = api_pb2.ModelHasRequest(
            storeID=store_id,
            modelName=model_name,
            entityIDs=entity_ids,
        )
        resp = self.stub.ModelHas(req)
        return resp.exists

    def model_find(self, store_id, model_name, query_json=b"{}"):
        req = api_pb2.ModelFindRequest(
            storeID=store_id,
            modelName=model_name,
            queryJSON=query_json,
        )
        resp = self.stub.ModelFind(req)
        return [json.loads(e.decode('utf-8')) for e in resp.entities]

    def model_find_by_id(self, store_id, model_name, entity_id):
        req = api_pb2.ModelFindByIDRequest(
            storeID=store_id,
            modelName=model_name,
            entityID=entity_id,
        )
        resp = self.stub.ModelFindByID(req)
        return json.loads(resp.entity)

    def read_transation(self):
        raise Exception('Read transaction not implemented')
        req = api_pb2.ReadTransactionRequest()
        resp = self.stub.ReadTransaction(req)
        return resp

    def write_transation(self):
        raise Exception('Write transaction not implemented')
        req = api_pb2.WriteTransactionRequest()
        resp = self.stub.WriteTransaction(req)
        return resp

    def create_listen_filter(self, model_name, entity_id, action):
        listen_filter = api_pb2.ListenRequest.Filter(
            modelName=model_name,
            entityID=entity_id,
            action=action,
        )
        return listen_filter

    def listen(self, store_id, filters):
        req = api_pb2.ListenRequest(
            storeID=store_id,
            filters=filters,
        )
        resp = self.stub.Listen(req)
        return resp


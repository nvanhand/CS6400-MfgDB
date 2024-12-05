# https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python

from exif import Image
from tokens import credential
import PIL
import json
import os
import sys
import uuid
import pandas as pd
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from azure.storage.filedatalake import DataLakeServiceClient as DLService
from azure.storage.filedatalake.aio import DataLakeServiceClient as DLService_aio
from azure.storage.filedatalake import ContentSettings
from azure.identity import DefaultAzureCredential


class DataHandler:
    def __init__(self, endpoint, key):
        self.client = CosmosClient(url=endpoint, credential=key)

    def get_db(self, dbname):
        try:
            database = self.client.create_database(id=dbname)
        except exceptions.CosmosResourceExistsError:
            print(f'{dbname} already exists. Returning existing ')
            database = self.client.get_database_client(database=dbname)
        return database

    def make_container(self, database, container_name):
        try:
            container = database.create_container(
                id=container_name, partition_key=PartitionKey(path="/productName")
            )
        except exceptions.CosmosResourceExistsError:
            container = database.get_container_client(container_name)

        return container

class CosmosUpload:
    client = CosmosClient(url=ENDPOINT, credential=KEY)

    csv = pd.read_csv("../localStore/buildDoc.csv")
    csv.rename(columns={"Build ID:": "id"}, inplace=True)
    database = client.get_database_client("build")
    container = database.get_container_client("build")
    for i in range(len(csv)):
        item = csv.iloc[i]
        try:
            container.upsert_item(dict(item.dropna()))
        except:
            print('Bad thing happened')

class SQL_add:
    def __init__(self, connection_string):
        for key, value in connection_string.items():
            setattr(self, key, value)
    def connect(self):
        conn = pymssql.connect(server=self.server, user=self.user,
                           password=self.password, database=self.database)
        cursor = conn.cursor()
        cursor.execute()

class StorageClient:
    def __init__(self, container='', dir='', use_async=False):
        self.fsys_client = None
        # read SAS token
        token_credential = DefaultAzureCredential()
        self.is_async = use_async
        SAS = open('tokens/ampfstorage_SAS', 'r').read()
        account_url = f"https://ampfstorage.dfs.core.windows.net"
        if use_async:
            self.client = DLService_aio(account_url, credential=SAS)
        else:
            self.client = DLService(account_url, credential=SAS)
        if container != '':
            self.cd(container=container)
        if dir != '':
            self.cd(dir=dir)

    def cd(self, container='', dir='', override=False):
        # Override:
        if self.fsys_client is None:
            self.fsys_client = self.client.get_file_system_client(container)
        if dir != '':
            self.dir_client = self.fsys_client.get_directory_client(dir)


    def upload(self, local_path, target_name=None, metadata={}):
        '''
        :param local_path: device file path
        :param target_name: name. if unspecified, match local path name
        :param metadata:
        :return:
        '''
        local_path = os.path.abspath(local_path)
        if target_name is None:
            name = os.path.basename(local_path)
        else:
            name = target_name

        ftype = name.split('.')[-1].lower() # Get path ending
        item = (open(local_path, 'rb')).read()
        im_metadata = Image (item).get_all()
        for k, v in list(im_metadata.items()):
            if k not in ['components_configuration', 'flashpix_version']:
                metadata[k] = str(v)

        file_client = self.dir_client.get_file_client(name)
        settings = ContentSettings(content_type=f'image/{ftype}')

        file_client.upload_data(data=item, length=os.stat(local_path).st_size,
                                         content_settings=settings,
                                         metadata=metadata, overwrite=True)

        return file_client


if __name__ == "__main__":
    sql_conn = {'server': 'nikkivh.database.windows.net',
                'user': 'nikkuser',
                'password': 'SQLadminpass0'}
    os.chdir('/Users/nikkivanhandel/ampf/ampfApp')
    client = StorageClient()

    fname='IMG_2677.JPG'
    item_path = f"localStore/{fname}"

    metadata = {
        "operator": "John Doe",
        "device": 'PHX-200S-MC',
        "description": "Example image for testing"
    }

    client.cd(container='eos-cam', dir='PHX200S-MC/')
    client.upload(local_path=item_path, target_name='example', metadata=metadata)

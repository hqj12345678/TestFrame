import pymongo
from config import setting
import configparser
class SearchMongo():
    def __init__(self):
        conn = configparser.ConfigParser()
        conn.read(setting.Config_Path, encoding="utf-8")
        client=conn.get("MongoDbSetting", "client")
        self.client=pymongo.MongoClient(client)
        db_name=conn.get("MongoDbSetting", "database_name")
        self.db=self.client[db_name]
        tb_name=conn.get("MongoDbSetting", "table_name")
        self.collection=self.db[tb_name]

    def search(self,search_dicts):
        results=self.collection.find(search_dicts)
        n=len(list(results))
        for result in results:
            print(result)
        if n==0:
            #不在数据库
            return False
        else:
            #在数据库
            return  True

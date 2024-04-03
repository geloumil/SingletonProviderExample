import time
from config.envLoader import EnvLoader
from mongo.mongo_provider import MongoProvider


class ConfigLoader:
    mongo_provider = None

    def __init__(self, full_init=True):
        if not ConfigLoader.mongo_provider:
            ConfigLoader.mongo_provider = MongoProvider(
                EnvLoader.mongo_db,
                username=EnvLoader.username,
                password=EnvLoader.password,
                host=EnvLoader.host,
                port=EnvLoader.port,
                authentication_source=EnvLoader.authentication_source
            )

import os


class EnvLoader:
    env_loaded = None
    mongo_db = None
    username = None
    password = None
    host = None
    port = None
    authentication_source = None

    def __init__(self):
        if not EnvLoader.env_loaded:
            EnvLoader.env_loaded = True
            EnvLoader.mongo_db = os.environ.get('MONGO_DB')
            EnvLoader.username = os.environ.get('MONGO_USR')
            EnvLoader.password = os.environ.get('MONGO_PSW')
            EnvLoader.host = os.environ.get('MONGO_HOST')
            EnvLoader.port = int(os.environ.get('MONGO_PORT'))
            EnvLoader.authentication_source = os.environ.get('MONGO_AUTH')

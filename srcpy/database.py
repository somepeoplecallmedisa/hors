import redis
from redis.utils import get_lib_version 

class Database(redis.StrictRedis):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, name: bytes | str | memoryview):
        return super().__getitem__(name)
    
    def __setitem__(self, name: bytes | str | memoryview, value: bytes | memoryview | str | int | float):
        return super().__setitem__(name, value)
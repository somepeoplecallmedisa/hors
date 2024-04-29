import fastapi
from database import Database
import os
from signal import SIGINT

class Router():
    def __init__(self):
        self.router = fastapi.APIRouter()
        self.db = Database()

        self.router.add_api_route("/local/debug", self.debug)
        self.router.add_api_route("/local/kill", self.kill)

    async def debug(self, req: fastapi.Request):
        if not req.client:
            return {"detail" : "not allowed"}
        if not req.client.host == "127.0.0.1":
            return {"detail" : "not allowed"}

        keys = self.db.keys()
        return_dict = {}

        for key in keys:
            return_dict[key] = self.db[key]

        return return_dict

    async def kill(self, req: fastapi.Request):
        if not req.client:
            return {"detail" : "not allowed"}
        if not req.client.host == "127.0.0.1":
            return {"detail" : "not allowed"}

        os.kill(os.getpid(), SIGINT)

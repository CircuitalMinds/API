from config import app_home
import logging
import asyncio
logfile = app_home.joinpath("history/app.log")
logfile.open("w").write("")


class History:

    log = logging
    log.basicConfig(
        filename=str(logfile),
        level=log.INFO,
        format='''{
    "message-type": "%(levelname)s",
    "location": "%(pathname)s:%(lineno)d",
    "module": "%(module)s",
    "function": "%(funcName)s",
    "time": "%(asctime)s.%(msecs)d",            
    "message": "'%(message)s'"
},''',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

    def __init__(self):
        logfile.open("w").write("")
        asyncio.run(self.init())

    async def init(self):
        await self.getinfo()
        self.log.info("Started")

    async def getinfo(self):
        self.log.info("Starting")
        return True

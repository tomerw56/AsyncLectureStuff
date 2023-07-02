import time
import asyncio
import asyncio.log as log
async def Mygoal():
   log.logger.info("pre wait")
   await asyncio.sleep(1)
   log.logger.info("Coroutines Implemented")

log.basicConfig(level=log.DEBUG)
loop = asyncio.get_event_loop()
try:
    loop.set_debug(True)
    loop.run_until_complete(Mygoal())
finally:
   loop.close()
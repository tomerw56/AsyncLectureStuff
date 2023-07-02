import time
import asyncio
import logging
class EventLoopDelayMonitor:

    def __init__(self, loop=None, start=True, interval=1, logger=None):
        self._interval = interval
        self._log = logger or logging.getLogger(__name__)
        self._loop = loop or asyncio.get_event_loop()
        if start:
            self.start()

    def run(self):
        self._loop.call_later(self._interval, self._handler, self._loop.time())

    def _handler(self, start_time):
        latency = (self._loop.time() - start_time) - self._interval
        self._log.error('EventLoop delay %.4f', latency)
        if not self.is_stopped():
            self.run()

    def is_stopped(self):
        return self._stopped

    def start(self):
        self._stopped = False
        self.run()

    def stop(self):
        self._stopped = True
async def main():
    EventLoopDelayMonitor(interval=1)
    await asyncio.sleep(1)
    time.sleep(2)
    await asyncio.sleep(1)
    await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
import asyncio
import time


class RateLimiter():
    """
    100 requests per minute
    """

    req_no = 0

    def __init__(self):
        pass

    async def update_rl(self):  # handle concurrency
        while True:
            await asyncio.sleep(1)
            self.req_no = 0
            print("reset done")

    async def req(self):
        self.req_no += 1
        if await self.validate():
            return True
        else:
            raise Exception("Throttle error")

    async def validate(self):
        if self.req_no <= 10:
            return True
        else:
            return False

    async def run_req(self, iterations):
        for i in range(iterations):
            await self.req()
            print(i,self.req_no)

    async def run_req2(self, iterations):
        await asyncio.sleep(10)
        for i in range(iterations):
            await self.req()
            print(i,self.req_no)

async def main():
    rl =  RateLimiter()
    print("start", time.time())

    L = await asyncio.gather(
        rl.run_req(10),
        rl.update_rl(),
        rl.run_req2(5),
    )

    print(L)
    print("end", time.time())

asyncio.run(main())

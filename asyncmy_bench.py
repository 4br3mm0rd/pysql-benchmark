import asyncio
import random
import time
from asyncio import Queue

import asyncmy

from benchmark_async import AsyncBenchmark


class AsyncMyBench(AsyncBenchmark):
    async def run(self):
        # Create a connection pool manually
        self.pool = await asyncmy.create_pool(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            db=self.DB_NAME,
            maxsize=self.num_batches,
        )
        res = {
            "insert": await self.insert(),
            "select": await self.select(),
            "update": await self.update(),
            "delete": await self.delete(),
        }

        self.pool.close()
        await self.pool.wait_closed()
        return res

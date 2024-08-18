import random
import time

import aiomysql

from benchmark_async import AsyncBenchmark


class AIOMySQLBench(AsyncBenchmark):
    async def run(self):
        # Create a connection pool using the specified pool class
        self.pool = await aiomysql.create_pool(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            db=self.DB_NAME,
            minsize=1,
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

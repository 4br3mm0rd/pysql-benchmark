import asyncio
import random
import time

import asyncmy

from benchmark_base import BenchmarkBase


class AsyncBenchmark(BenchmarkBase):
    def __init__(self, num_batches=10):
        super().__init__()
        self.num_batches = num_batches  # Number of queries to run in parallel at once

    async def insert(self):
        start_time = time.time()

        async def insert_query(_):
            async with self.pool.acquire() as connection:
                async with connection.cursor() as cursor:
                    data = f"Sample data {random.randint(1, 1000)}"
                    await cursor.execute(self.insert_query, (data,))
                    await connection.commit()

        await self._run_in_batches(insert_query)

        end_time = time.time()
        return end_time - start_time

    async def select(self):
        start_time = time.time()

        async def select_query(i):
            async with self.pool.acquire() as connection:
                async with connection.cursor() as cursor:
                    await cursor.execute(self.select_query, (i,))
                    await cursor.fetchone()

        await self._run_in_batches(select_query)

        end_time = time.time()
        return end_time - start_time

    async def update(self):
        start_time = time.time()

        async def update_query(i):
            async with self.pool.acquire() as connection:
                async with connection.cursor() as cursor:
                    new_data = f"Updated data {random.randint(1, 1000)}"
                    await cursor.execute(self.update_query, (new_data, i))
                    await connection.commit()

        await self._run_in_batches(update_query)

        end_time = time.time()
        return end_time - start_time

    async def delete(self):
        start_time = time.time()

        async def delete_query(_):
            async with self.pool.acquire() as connection:
                async with connection.cursor() as cursor:
                    await cursor.execute(self.delete_query)
                    await connection.commit()

        await self._run_in_batches(delete_query)

        end_time = time.time()
        return end_time - start_time

    async def _run_in_batches(self, query_func):
        # Run queries in smaller batches
        for i in range(0, self.NUM_QUERIES, self.num_batches):
            batch = range(i + 1, min(i + self.num_batches + 1, self.NUM_QUERIES + 1))
            await asyncio.gather(*(query_func(j) for j in batch))

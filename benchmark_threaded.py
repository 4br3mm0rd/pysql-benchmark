import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from benchmark_base import BenchmarkBase


class ThreadedBenchmark(BenchmarkBase):
    def __init__(self):
        super().__init__()
        self.NUM_THREADS = 10
        self.connection_pool = {}

    def _disconnect(self):
        for thread in self.connection_pool:
            connection, cursor = self.connection_pool[thread]
            cursor.close()
            connection.close()

    def _get_connection_from_pool(self):
        thread_id = threading.get_ident()
        if thread_id not in self.connection_pool:
            self.connection_pool[thread_id] = self._connect()
        return self.connection_pool[thread_id]

    def run(self):
        self._disconnect()
        return {
            "insert": self.insert(),
            "select": self.select(),
            "update": self.update(),
            "delete": self.delete(),
        }

    def _run_queries_in_threads(self, query_func):
        with ThreadPoolExecutor(max_workers=self.NUM_THREADS) as executor:
            futures = [
                executor.submit(query_func, i) for i in range(1, self.NUM_QUERIES + 1)
            ]
            for future in as_completed(futures):
                future.result()

    def insert(self):
        connection, cursor = self._connect()

        # Drop the table if it exists and create it again
        cursor.execute(self.drop_table_query)
        cursor.execute(self.create_table_query)
        cursor.close()
        connection.close()

        start_time = time.time()

        def insert_query(_):
            connection, cursor = self._get_connection_from_pool()
            data = f"Sample data {random.randint(1, 1000)}"
            cursor.execute(self.insert_query, (data,))
            connection.commit()

        self._run_queries_in_threads(insert_query)
        end_time = time.time()

        return end_time - start_time

    def select(self):
        connection, cursor = self._connect()

        cursor.close()
        connection.close()
        start_time = time.time()

        def select_query(i):
            connection, cursor = self._get_connection_from_pool()
            cursor.execute(self.select_query, (i,))
            cursor.fetchone()

        self._run_queries_in_threads(select_query)

        end_time = time.time()

        return end_time - start_time

    def update(self):
        connection, cursor = self._connect()
        cursor.close()
        connection.close()
        start_time = time.time()

        def update_query(i):
            connection, cursor = self._get_connection_from_pool()
            new_data = f"Updated data {random.randint(1, 1000)}"
            cursor.execute(self.update_query, (new_data, i))
            connection.commit()

        self._run_queries_in_threads(update_query)

        end_time = time.time()

        return end_time - start_time

    def delete(self):
        connection, cursor = self._connect()
        cursor.close()
        connection.close()

        start_time = time.time()

        def delete_query(_):
            connection, cursor = self._get_connection_from_pool()
            cursor.execute(self.delete_query)
            connection.commit()

        self._run_queries_in_threads(delete_query)
        end_time = time.time()

        return end_time - start_time

import random
import time

from benchmark_base import BenchmarkBase


class Benchmark(BenchmarkBase):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        return {
            "insert": self.insert(),
            "select": self.select(),
            "update": self.update(),
            "delete": self.delete(),
        }

    def insert(self):
        connection, cursor = self._connect()

        # Drop the table if it exists and create it again
        cursor.execute(self.drop_table_query)
        cursor.execute(self.create_table_query)

        start_time = time.time()

        # Insert 1000 rows using pymysql
        for _ in range(self.NUM_QUERIES):
            data = f"Sample data {random.randint(1, 1000)}"
            cursor.execute(self.insert_query, (data,))

        connection.commit()
        end_time = time.time()

        cursor.close()
        connection.close()

        return end_time - start_time

    def select(self):
        connection, cursor = self._connect()

        start_time = time.time()

        # Execute 1000 SELECT queries using pymysql
        for i in range(1, self.NUM_QUERIES + 1):
            cursor.execute(self.select_query, (i,))
            cursor.fetchone()

        end_time = time.time()

        cursor.close()
        connection.close()

        return end_time - start_time

    def update(self):
        connection, cursor = self._connect()

        start_time = time.time()

        for i in range(1, self.NUM_QUERIES + 1):
            new_data = f"Updated data {random.randint(1, 1000)}"
            cursor.execute(self.update_query, (new_data, i))
        connection.commit()
        end_time = time.time()

        cursor.close()
        connection.close()

        return end_time - start_time

    def delete(self):
        connection, cursor = self._connect()

        start_time = time.time()

        for i in range(1, self.NUM_QUERIES + 1):
            cursor.execute(self.delete_query)

        connection.commit()
        end_time = time.time()

        cursor.close()
        connection.close()

        return end_time - start_time

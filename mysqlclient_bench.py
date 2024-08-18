import random
import time

import MySQLdb

from benchmark import Benchmark


class MySQLdbBench(Benchmark):
    def _connect(self):
        connection = MySQLdb.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            database=self.DB_NAME,
        )
        cursor = connection.cursor()
        return connection, cursor

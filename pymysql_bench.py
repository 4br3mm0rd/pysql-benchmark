import random
import time

import pymysql

from benchmark import Benchmark


class PyMySQLBench(Benchmark):

    def _connect(self):
        connection = pymysql.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            database=self.DB_NAME,
        )
        cursor = connection.cursor()
        return connection, cursor

import pymysql

from benchmark_threaded import ThreadedBenchmark


class MySQLdbThreadedBench(ThreadedBenchmark):
    def _connect(self):
        connection = pymysql.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            database=self.DB_NAME,
        )
        cursor = connection.cursor()
        return connection, cursor

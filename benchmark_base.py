class BenchmarkBase:
    def __init__(self) -> None:
        self.DB_HOST = "127.0.0.1"
        self.DB_USER = "root"
        self.DB_PASSWORD = ""
        self.DB_NAME = "benchmark_test"
        self.NUM_QUERIES = 10000

        self.create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data VARCHAR(100)
        )
        """
        self.drop_table_query = "DROP TABLE IF EXISTS test_table"

        self.insert_query = "INSERT INTO test_table (data) VALUES (%s)"
        self.select_query = "SELECT * FROM test_table WHERE id = %s"
        self.delete_query = "DELETE FROM test_table WHERE 1 LIMIT 1"
        self.update_query = "UPDATE test_table SET data = %s WHERE id = %s"

    def _connect():
        raise NotImplementedError()

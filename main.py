import asyncio

from aiomysql_bench import AIOMySQLBench
from asyncmy_bench import AsyncMyBench
from mysqlclient_bench import MySQLdbBench
from mysqlclient_threaded_bench import MySQLdbThreadedBench
from pymysql_bench import PyMySQLBench
from pymysql_threaded_bench import PyMySQLThreadedBench


async def main():
    pymysql_bench = PyMySQLBench()
    pymysql_threaded_bench = PyMySQLThreadedBench()
    mysqlclient_bench = MySQLdbBench()
    mysqlclient_threaded_bench = MySQLdbThreadedBench()
    asyncmy_bench = AsyncMyBench()
    aiomysql_bench = AIOMySQLBench()

    # print("Running PyMySQL bench...")
    # print(pymysql_bench.run())

    # print("Running mysqlclient bench...")
    # print(mysqlclient_bench.run())

    # print("Let's go for async mode!")
    # print("Running threaded PyMySQL...")
    # print(pymysql_threaded_bench.run())

    # print("Running threaded mysqlclient...")
    # print(mysqlclient_threaded_bench.run())

    print("Running asyncmy bench...")
    print(await asyncmy_bench.run())

    print("Running aiomysql bench...")
    print(await aiomysql_bench.run())


if __name__ == "__main__":
    asyncio.run(main())

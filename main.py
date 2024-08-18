import asyncio

import matplotlib.pyplot as plt

from aiomysql_bench import AIOMySQLBench
from asyncmy_bench import AsyncMyBench
from mysqlclient_bench import MySQLdbBench
from mysqlclient_threaded_bench import MySQLdbThreadedBench
from pymysql_bench import PyMySQLBench
from pymysql_threaded_bench import PyMySQLThreadedBench


def plot_histogram(data, libraries, queries):
    fig, ax = plt.subplots()

    # Create bar positions
    x = range(len(queries))
    total_width = 0.8  # Total width for all bars in a group
    width = total_width / len(libraries)  # Width of each bar

    # Plot data for each library
    for i, library in enumerate(libraries):
        times = [data[library][query] for query in queries]
        ax.bar([pos + i * width for pos in x], times, width, label=library)

    # Set labels and title
    ax.set_xlabel("Queries")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Query Performance by Library")
    ax.set_xticks([pos + total_width / 2 for pos in x])
    ax.set_xticklabels(queries)

    # Add legend
    ax.legend()

    plt.show()


async def main():
    pymysql_bench = PyMySQLBench()
    pymysql_threaded_bench = PyMySQLThreadedBench()
    mysqlclient_bench = MySQLdbBench()
    mysqlclient_threaded_bench = MySQLdbThreadedBench()
    asyncmy_bench = AsyncMyBench()
    aiomysql_bench = AIOMySQLBench()

    print("Running PyMySQL bench...")
    pymy_res = pymysql_bench.run()
    print(pymy_res)

    print("Running mysqlclient bench...")
    mc_res = mysqlclient_bench.run()
    print(mc_res)

    print("Let's go for async mode!")
    print("Running threaded PyMySQL...")
    pymyt_res = pymysql_threaded_bench.run()
    print(pymyt_res)

    print("Running threaded mysqlclient...")
    mysqlt_res = mysqlclient_threaded_bench.run()
    print(mysqlt_res)

    print("Running asyncmy bench...")
    am_res = await asyncmy_bench.run()
    print(am_res)

    print("Running aiomysql bench...")
    aiom_res = await aiomysql_bench.run()
    print(aiom_res)

    print("Plotting results...")
    data = {
        "PyMySQL": pymy_res,
        "mysqlclient": mc_res,
        "PyMySQL T": pymyt_res,
        "mysqlclient T": mysqlt_res,
        "asyncmy": am_res,
        "aiomysql": aiom_res,
    }
    libraries = [lib for lib in data]
    queries = ["insert", "select", "update", "delete"]
    plot_histogram(data, libraries, queries)


if __name__ == "__main__":
    asyncio.run(main())

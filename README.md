# pysql-benchmark

This repository contains the benchmark of the following solutions for mysql drivers in Python:

- PyMySQL
- mysqlclient within a threadpool
- mysqlclient
- mysqlclient within a threadpool
- aiomysql
- asyncmy

# motivation

Because the page of asyncmy offers a benchmark which is limited to only one query, we cannot really estimate the impact of asyncio on the performance.
This is where this project comes into life.

# results

The benchmark has been run on a Macbook Pro M1 Pro 32GB

# Fibonacci Performance Comparison

This project compares the performance of calculating Fibonacci numbers using two different approaches: LRU Cache and Splay Tree.

## Task 1: Data Access Optimization with LRU Cache

- Implement functions to handle array queries with and without LRU Cache.
- Measure execution time for both approaches and output results.

## Task 2: Fibonacci Calculation with LRU Cache and Splay Tree

- Implement `fibonacci_lru` using `@lru_cache` decorator.
- Implement `fibonacci_splay` using Splay Tree for caching.
- Measure execution time for Fibonacci numbers from 0 to 950 with a step of 50.
- Plot a graph comparing execution times for both approaches.
- Output a formatted table with results.

## Requirements

- Python 3.x
- `matplotlib` for plotting graphs

## Usage

1. Run the script to execute both tasks.
2. Observe the console output for execution times and the plotted graph for performance comparison.

## Conclusion

The project demonstrates the efficiency of caching techniques in optimizing computational tasks. The LRU Cache approach is generally faster due to its simplicity and built-in optimization, while the Splay Tree provides a more complex but flexible caching mechanism.

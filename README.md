# Farmable Land Calculator

## Description

This project simulates a piece of land as a randomly generated 2D matrix of 0s and 1s. It processes this matrix to identify and calculate the dimensions of the largest possible square of "farmable" land.

In this simulation:
* **1** represents farmable land.
* **0** represents non-farmable land (obstacles, water, etc.).

The program generates a matrix with random dimensions, saves the output to a text file, and prints the size of the largest contiguous square of farmable land found.

## Features

* **Random Map Generation:** Creates a grid of random dimensions (rows: 15-40, columns: 15-60). Although, these dimensions are changeable.
* **Square Detection Algorithm:** scans the matrix to calculate the maximum square dimensions for every coordinate containing a `1`.
* **Analysis:** Identifies the largest contiguous square of farmable land available on the entire map.
* **File Export:** Saves the generated matrix to `farm_land_matrix.txt` for visual inspection.

## Project Structure

```text
farmable-land-calculator/
├── farm_land_matrix.txt   # Output file containing the generated 0/1 matrix
└── lib/
    ├── farm_land.py       # Core logic and algorithm functions
    └── main.py            # Entry point script to run the program

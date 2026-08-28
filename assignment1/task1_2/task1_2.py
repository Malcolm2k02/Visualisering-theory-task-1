"""Starter script for Task 1.2 — Parallel Coordinates and Dimensional Stacking (placeholders).

This script reads the provided CSV and prints the DataFrame. Add plotting code to the provided functions to
create the Parallel Coordinates and Dimensional Stacking visualizations.
"""

import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "task1_2_sales.csv")
FIG_DIR = os.path.join(os.path.dirname(__file__), "figures")


def ensure_fig_dir():
    os.makedirs(FIG_DIR, exist_ok=True)


def identify_variable_types(df):
    """Identify variable types according to Tamara Munzner's hierarchical task/variable scheme.

    TODO: Replace prints with a small function that returns the types or writes them to notes.md
    Example (informal):
      - Region: categorical (nominal)
      - Product: categorical (nominal)
      - Size: ordinal or categorical depending on interpretation (S/M or numeric 32/34)
      - Business Model: categorical (nominal)
      - Sales: quantitative (numeric)
    """
    print("--- Variable type identification (TODO: formalize in notes.md) ---")
    print("Region: nominal (categorical)")
    print("Product: nominal (categorical)")
    print("Size: ordinal or categorical depending on interpretation")
    print("Business Model: nominal (categorical)")
    print("Sales: quantitative (numeric)")


def create_parallel_coordinates(df):
    """Create a Parallel Coordinates Plot and save it to task1_2/figures/parallel_coordinates.png

    TODO: Implement the plot using matplotlib or pandas.plotting.parallel_coordinates.
    """
    ensure_fig_dir()
    # TODO: implement the parallel coordinates plot
    print("TODO: create_parallel_coordinates() — implement and save to figures/")


def create_dimensional_stacking(df):
    """Create a Dimensional Stacking visualization and save it to task1_2/figures/dimensional_stacking.png

    TODO: Implement a dimensional stacking visualization. There are multiple ways to approximate this with matplotlib.
    """
    ensure_fig_dir()
    # TODO: implement the dimensional stacking plot
    print("TODO: create_dimensional_stacking() — implement and save to figures/")


def main():
    print("Task 1.2 starter script — reading CSV and printing DataFrame")
    print("Data path:", DATA_PATH)
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print("Data file not found. Make sure assignment1/data/task1_2_sales.csv exists.")
        return

    print("Data loaded. First rows:")
    print(df.head())
    identify_variable_types(df)
    # Once plotting functions are implemented, call them here:
    # create_parallel_coordinates(df)
    # create_dimensional_stacking(df)


if __name__ == "__main__":
    main()

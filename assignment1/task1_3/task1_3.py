"""Starter script for Task 1.3 — placeholder code for fixing two visualizations.

This script provides helper functions and instructions. Add the original CSVs and images to assignment1/data/task1_3/ and
implement the fix_visualization_1 and fix_visualization_2 functions to load the originals, analyze problems, and create improved plots.
"""

import os
import glob

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "task1_3")
FIG_DIR = os.path.join(os.path.dirname(__file__), "figures")


def ensure_fig_dir():
    os.makedirs(FIG_DIR, exist_ok=True)


def list_available_originals():
    """List CSV and image files placed in the data/task1_3 directory."""
    print("Looking for original files in:", DATA_DIR)
    patterns = ("*.csv", "*.png", "*.jpg", "*.jpeg")
    found = []
    for p in patterns:
        found.extend(glob.glob(os.path.join(DATA_DIR, p)))
    if not found:
        print("No original CSVs or images found. Add files to assignment1/data/task1_3/")
    else:
        for f in found:
            print("  ", os.path.relpath(f))


def fix_visualization_1(orig_csv_path):
    """Placeholder for implementing fixes to the first chosen visualization.

    Steps to implement:
    1. Load CSV using pandas.
    2. Identify problems (expressiveness, effectiveness, appropriateness).
    3. Create improved figure using matplotlib and save to task1_3/figures/improved_viz_1.png
    """
    ensure_fig_dir()
    # TODO: implement
    print("TODO: fix_visualization_1() — implement when you select the first visualization to fix.")


def fix_visualization_2(orig_csv_path):
    """Placeholder for implementing fixes to the second chosen visualization."""
    ensure_fig_dir()
    # TODO: implement
    print("TODO: fix_visualization_2() — implement when you select the second visualization to fix.")


def main():
    print("Task 1.3 starter script")
    list_available_originals()
    print("Place original CSVs and images in assignment1/data/task1_3/ and then implement fix_visualization_1/2().")


if __name__ == "__main__":
    main()

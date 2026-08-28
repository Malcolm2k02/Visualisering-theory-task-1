"""Starter script for Task 1.1 — intentionally bad visualizations (placeholders).

This file contains beginner-friendly placeholder functions and TODO comments. Replace the placeholders with your
intentionally bad visualizations and short written explanations saved in notes.md.
"""

import os
import matplotlib
# Use non-interactive backend for scripts that save files (works in CI or headless environments)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

FIG_DIR = os.path.join(os.path.dirname(__file__), "figures")


def ensure_fig_dir():
    os.makedirs(FIG_DIR, exist_ok=True)


def create_non_expressive_example():
    """Create a deliberately non-expressive visualization.

    TODO: Replace this placeholder with your intentionally bad plot. Save the final figure to:
      task1_1/figures/non_expressive.png

    Provide a short written explanation in task1_1/notes.md explaining why the plot is non-expressive.
    """
    ensure_fig_dir()
    # Minimal placeholder figure to verify saving works
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    ax.set_title("NON-EXPRESSIVE placeholder (TODO)")
    fig_path = os.path.join(FIG_DIR, "non_expressive_placeholder.png")
    fig.savefig(fig_path)
    plt.close(fig)
    print(f"Wrote placeholder: {fig_path}")


def create_inefficient_example():
    """Create a deliberately inefficient visualization.

    TODO: Implement an example that demonstrates inefficiency (e.g., massive overplotting, redundant encodings).
    Save to task1_1/figures/inefficient.png
    """
    # TODO: implement
    print("TODO: create_inefficient_example() — implement an inefficient visualization and save it to figures/")


def create_inappropriate_example():
    """Create a deliberately inappropriate visualization.

    TODO: Implement an inappropriate example (e.g., using 3D for 2D relationships, or misleading scales).
    Save to task1_1/figures/inappropriate.png
    """
    # TODO: implement
    print("TODO: create_inappropriate_example() — implement an inappropriate visualization and save it to figures/")


def main():
    print("Task 1.1 starter script")
    create_non_expressive_example()
    # The other functions are TODOs: call them after implementation
    # create_inefficient_example()
    # create_inappropriate_example()
    print("See task1_1/notes.md for guidance on explanations and where to write them.")


if __name__ == "__main__":
    main()

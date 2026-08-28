"""Starter script for Task 1.1 — intentionally bad visualizations (placeholders).

This file contains beginner-friendly placeholder functions and TODO comments. Replace the placeholders with your
intentionally bad visualizations and short written explanations saved in notes.md.
"""

import os
import matplotlib
import numpy as np
# Use non-interactive backend for scripts that save files (works in CI or headless environments)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

FIG_DIR = os.path.join(os.path.dirname(__file__), "figures")

# Illustrative average retail oil prices in USD per barrel.
OIL_PRICES = pd.DataFrame(
    {
        "country": [
            "Canada",
            "United States",
            "Mexico",
            "Brazil",
            "United Kingdom",
            "Norway",
            "Germany",
            "France",
            "Spain",
            "Italy",
            "Saudi Arabia",
            "United Arab Emirates",
            "Kuwait",
            "India",
            "China",
            "Japan",
            "Australia",
            "South Africa",
            "Nigeria",
            "Egypt",
        ],
        "oil_price_usd_per_barrel": [
            78.4,
            81.2,
            83.7,
            86.5,
            92.1,
            94.6,
            96.3,
            95.8,
            89.4,
            91.7,
            63.2,
            64.1,
            62.8,
            88.9,
            84.6,
            97.5,
            99.3,
            82.7,
            79.8,
            76.5,
        ],
    }
)


def ensure_fig_dir():
    os.makedirs(FIG_DIR, exist_ok=True)


def create_non_expressive_example():
    """Create a deliberately non-expressive visualization.
    Provide a short written explanation in task1_1/notes.md explaining why the plot is non-expressive.
    """
    fig, ax = plt.subplots()
    ax.plot(OIL_PRICES["country"], OIL_PRICES["oil_price_usd_per_barrel"])
    ax.set_title("Oil Prices by Country")
    ax.set_xlabel("Country")
    ax.set_ylabel("Oil Price (USD per Barrel)")
    ensure_fig_dir()
    fig_path = os.path.join(FIG_DIR, "non_expressive.png")
    ax.set_ylim(60, 100)
    fig.savefig(fig_path)
    plt.close(fig)


def create_inefficient_example():
    """Create a deliberately inefficient visualization.

    Oil prices are represented using bubble area, while the position of each
    country is arbitrary. This makes comparison between countries unnecessarily
    difficult compared with, for example, a sorted bar chart.

    Saves to task1_1/figures/inefficient.png
    """

    # Make random positions reproducible
    np.random.seed(42)

    # Random positions carry no information
    x = np.random.uniform(0, 10, len(OIL_PRICES))
    y = np.random.uniform(0, 10, len(OIL_PRICES))

    # Represent oil price using bubble area
    sizes = OIL_PRICES["oil_price_usd_per_barrel"] ** 2

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.scatter(
        x,
        y,
        s=sizes,
        alpha=0.6
    )

    # Put the country name inside each bubble
    for i, country in enumerate(OIL_PRICES["country"]):
        ax.text(
            x[i],
            y[i],
            country,
            ha="center",
            va="center",
            fontsize=8
        )

    ax.set_title("Oil Prices by Country")

    # Hide axes because position has no meaning
    ax.set_xticks([])
    ax.set_yticks([])

    fig.tight_layout()

    # Save figure
    fig_path = os.path.join(
        FIG_DIR,
        "inefficient.png"
    )

    fig.savefig(
        fig_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved inefficient visualization to {fig_path}")


def create_inappropriate_example():
    """Create a deliberately inappropriate visualization.

    Monthly temperatures are shown using a pie chart. A pie chart is intended
    for part-to-whole relationships, while temperatures across months are an
    ordered sequence and do not form a meaningful whole.

    Saves to task1_1/figures/inappropriate.png
    """

    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    temperatures = [
        2, 3, 6, 10, 15, 19,
        22, 21, 17, 11, 6, 3
    ]

    fig, ax = plt.subplots(figsize=(9, 9))

    ax.pie(
        temperatures,
        labels=months,
        autopct="%1.1f%%"
    )

    ax.set_title("Average Monthly Temperature")

    fig.tight_layout()

    # Save figure
    fig_path = os.path.join(
        FIG_DIR,
        "inappropriate.png"
    )

    fig.savefig(
        fig_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved inappropriate visualization to {fig_path}")


def main():
    print("Task 1.1 starter script")
    create_non_expressive_example()
    create_inefficient_example()
    create_inappropriate_example()
    print("See task1_1/notes.md for guidance on explanations and where to write them.")


if __name__ == "__main__":
    main()

"""Starter script for Task 1.2 — Parallel Coordinates and Dimensional Stacking (placeholders).

This script reads the provided CSV and prints the DataFrame. Add plotting code to the provided functions to
create the Parallel Coordinates and Dimensional Stacking visualizations.
"""

import os
import pandas as pd
import matplotlib
# Use non-interactive backend for scripts that save files (works in CI or headless environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "task1_2_sales.csv")
FIG_DIR = os.path.join(os.path.dirname(__file__), "figures")

COMPANY_SALES = pd.DataFrame(
    {
        "Region": [
            "EU",
            "EU",
            "EU",
            "EU",
            "EU",
            "EU",
            "EU",
            "EU",
            "US",
            "US",
            "US",
            "US",
            "US",
            "US",
            "US",
            "US",
        ],
        "Product": [
            "Jeans",
            "Jeans",
            "Jeans",
            "Jeans",
            "Shirt",
            "Shirt",
            "Shirt",
            "Shirt",
            "Jeans",
            "Jeans",
            "Jeans",
            "Jeans",
            "Shirt",
            "Shirt",
            "Shirt",
            "Shirt",
        ],
        "Size": [
            32,
            32,
            34,
            34,
            "S",
            "S",
            "M",
            "M",
            32,
            32,
            34,
            34,
            "S",
            "S",
            "M",
            "M",
        ],
        "Business Model": [
            "Online",
            "Store",
            "Online",
            "Store",
            "Online",
            "Store",
            "Online",
            "Store",
            "Online",
            "Store",
            "Online",
            "Store",
            "Online",
            "Store",
            "Online",
            "Store",
        ],
        "Sales": [
            5,
            15,
            2,
            10,
            2,
            10,
            2,
            5,
            5,
            2,
            15,
            5,
            5,
            2,
            10,
            5
        ],
    }
)
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


def create_parallel_coordinates():
    """Create a parallel coordinates plot for the company sales dataset."""

    df = COMPANY_SALES.copy()

    # Numerical positions used only for plotting
    mappings = {
        "Region": {"EU": 0, "US": 1},
        "Product": {"Jeans": 0, "Shirt": 1},
        "Size": {32: 0, 34: 1, "S": 2, "M": 3},
        "Business Model": {"Online": 0, "Store": 1},
    }

    dimensions = [
        "Region",
        "Product",
        "Size",
        "Business Model",
        "Sales"
    ]

    x_positions = range(len(dimensions))

    fig, ax = plt.subplots(figsize=(12, 7))

    # Draw one polyline for each row in the dataset
    for _, row in df.iterrows():

        values = [
            mappings["Region"][row["Region"]],
            mappings["Product"][row["Product"]],
            mappings["Size"][row["Size"]],
            mappings["Business Model"][row["Business Model"]],
            row["Sales"]
        ]

        # Normalize each dimension to 0-1 so they can share the same plot
        normalized_values = [
            values[0],                  # Region: 0-1
            values[1],                  # Product: 0-1
            values[2] / 3,              # Size: 0-3 -> 0-1
            values[3],                  # Business Model: 0-1
            (values[4] - 2) / (15 - 2)  # Sales: 2-15 -> 0-1
        ]

        ax.plot(
            x_positions,
            normalized_values,
            alpha=0.6
        )

    # Draw vertical axes
    for x in x_positions:
        ax.axvline(x=x, linewidth=1)

    # Dimension names
    ax.set_xticks(list(x_positions))
    ax.set_xticklabels(dimensions)

    # Main y-axis is hidden because each vertical axis has its own scale
    ax.set_yticks([])

    # Add labels manually for each dimension

    # Region
    ax.text(0, 0, "EU", ha="right", va="center")
    ax.text(0, 1, "US", ha="right", va="center")

    # Product
    ax.text(1, 0, "Jeans", ha="right", va="center")
    ax.text(1, 1, "Shirt", ha="right", va="center")

    # Size
    size_labels = ["32", "34", "S", "M"]
    for i, label in enumerate(size_labels):
        ax.text(
            2,
            i / 3,
            label,
            ha="right",
            va="center"
        )

    # Business Model
    ax.text(3, 0, "Online", ha="right", va="center")
    ax.text(3, 1, "Store", ha="right", va="center")

    # Sales
    sales_ticks = [2, 5, 10, 15]
    for value in sales_ticks:
        normalized = (value - 2) / (15 - 2)

        ax.text(
            4,
            normalized,
            str(value),
            ha="left",
            va="center"
        )

    ax.set_title("Parallel Coordinates Plot of Company Sales")

    ax.set_xlim(-0.3, 4.3)
    ax.set_ylim(-0.05, 1.05)

    fig.tight_layout()

    fig_path = os.path.join(
        FIG_DIR,
        "task1_2/figures/parallel_coordinates.png"
    )

    fig.savefig(
        fig_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved parallel coordinates plot to {fig_path}")

def create_dimensional_stacking(df):
    """Create a Dimensional Stacking visualization.

    Dimensions:
        x outer: Region
        x inner: Product
        y outer: Business Model
        y inner: Size

    Color represents Sales.

    Saves to task1_2/figures/dimensional_stacking.png
    """

    ensure_fig_dir()

    regions = ["EU", "US"]
    products = ["Jeans", "Shirt"]
    business_models = ["Online", "Store"]

    # Sizes depend on the product
    product_sizes = {
        "Jeans": [32, 34],
        "Shirt": ["S", "M"]
    }

    fig, ax = plt.subplots(figsize=(10, 8))

    # Track positions so we can label the cells
    cell_values = []

    for region_index, region in enumerate(regions):
        for product_index, product in enumerate(products):

            # Nested x-position:
            # Region is outer dimension, Product is inner dimension
            x = region_index * len(products) + product_index

            sizes = product_sizes[product]

            for business_index, business in enumerate(business_models):
                for size_index, size in enumerate(sizes):

                    # Nested y-position:
                    # Business Model is outer dimension, Size is inner dimension
                    y = business_index * 2 + size_index

                    row = df[
                        (df["Region"] == region)
                        & (df["Product"] == product)
                        & (df["Size"] == size)
                        & (df["Business Model"] == business)
                    ]

                    if not row.empty:
                        sales = row["Sales"].iloc[0]

                        cell_values.append(
                            {
                                "x": x,
                                "y": y,
                                "sales": sales,
                                "region": region,
                                "product": product,
                                "business": business,
                                "size": size
                            }
                        )

    # Draw each cell
    for cell in cell_values:
        rectangle = plt.Rectangle(
            (cell["x"], cell["y"]),
            1,
            1,
            edgecolor="black",
            linewidth=1
        )

        ax.add_patch(rectangle)

        # Add sales number in the middle
        ax.text(
            cell["x"] + 0.5,
            cell["y"] + 0.5,
            str(cell["sales"]),
            ha="center",
            va="center",
            fontsize=11
        )

    # Use an invisible scatter plot to create the color scale
    scatter = ax.scatter(
        [c["x"] + 0.5 for c in cell_values],
        [c["y"] + 0.5 for c in cell_values],
        c=[c["sales"] for c in cell_values],
        s=900,
        marker="s"
    )

    # Re-add text on top of colored squares
    for cell in cell_values:
        ax.text(
            cell["x"] + 0.5,
            cell["y"] + 0.5,
            f'{cell["size"]}\n{cell["sales"]}',
            ha="center",
            va="center"
        )

    # -----------------------
    # Axis labels
    # -----------------------

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)

    ax.set_xticks([
        0.5, 1.5,
        2.5, 3.5
    ])

    ax.set_xticklabels([
        "Jeans",
        "Shirt",
        "Jeans",
        "Shirt"
    ])

    ax.set_yticks([
        0.5, 1.5,
        2.5, 3.5
    ])

    ax.set_yticklabels([
        "Size 1",
        "Size 2",
        "Size 1",
        "Size 2"
    ])

    # Outer dimension separators
    ax.axvline(2, linewidth=2)
    ax.axhline(2, linewidth=2)

    # Outer Region labels
    ax.text(
        1,
        -0.55,
        "EU",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

    ax.text(
        3,
        -0.55,
        "US",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

    # Outer Business Model labels
    ax.text(
        -0.6,
        1,
        "Online",
        va="center",
        rotation=90,
        fontsize=12,
        fontweight="bold"
    )

    ax.text(
        -0.6,
        3,
        "Store",
        va="center",
        rotation=90,
        fontsize=12,
        fontweight="bold"
    )

    ax.set_title("Dimensional Stacking of Company Sales")

    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label("Sales (1000 €)")

    fig.tight_layout()

    fig_path = os.path.join(
        FIG_DIR,
        "dimensional_stacking.png"
    )

    fig.savefig(
        fig_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved dimensional stacking visualization to {fig_path}")

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
    create_dimensional_stacking(df)


if __name__ == "__main__":
    main()

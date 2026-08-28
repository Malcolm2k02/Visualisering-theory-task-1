# Assignment 1 — Visualization Theory (starter project)

This repository contains starter code and a clean project structure for the university visualization assignment (Assignment 1). The repository is intentionally minimal: it provides a place for your data, starter Python scripts, TODO placeholders for the visualizations, and directories where generated figures should be saved.

Overview
- Task 1.1: Create three intentionally bad visualizations (non-expressive, inefficient, inappropriate). Provide short explanations for why each is bad.
- Task 1.2: Work with a small sales dataset to (a) identify variable types, (b) create a Parallel Coordinates Plot, (c) create a Dimensional Stacking visualization, and (d) discuss which method is preferable.
- Task 1.3: Select two of six supplied course visualizations, identify problems, and recreate improved visualizations side-by-side with the originals.

Project layout

assignment1/
├── README.md                <- this file
├── requirements.txt         <- dependencies for the starter code
├── data/
│   ├── task1_2_sales.csv    <- dataset for Task 1.2
│   └── task1_3/
│       └── README.md        <- instructions for placing Task 1.3 originals
├── task1_1/
│   ├── task1_1.py           <- starter script and placeholders
│   ├── notes.md             <- guidance for the task and explanations
│   └── figures/             <- save generated figures here
├── task1_2/
│   ├── task1_2.py           <- starter script that reads the CSV and prints it
│   ├── notes.md             <- guidance for subtasks (a)-(d)
│   └── figures/             <- save generated figures here
├── task1_3/
│   ├── task1_3.py           <- starter script and placeholders for fixes
│   ├── notes.md             <- guidance and naming conventions
│   └── figures/             <- save improved and comparison figures here
└── report/
    └── report_notes.md      <- notes and suggested structure for the final report

Where to save figures
- Save generated figures in the figures/ directory for the corresponding task, e.g.:
  - task1_1/figures/
  - task1_2/figures/
  - task1_3/figures/

How to install dependencies
1. Create and activate a virtual environment (recommended):

   python -m venv venv

   # macOS / Linux
   source venv/bin/activate

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

How to run the starter scripts
- From the repository root, run:

  python task1_2/task1_2.py   # reads the CSV and prints the DataFrame
  python task1_1/task1_1.py   # creates placeholder figure for Task 1.1
  python task1_3/task1_3.py   # lists available original files for Task 1.3

Notes and constraints
- This project uses Python with pandas and matplotlib for the starter code.
- Code is intentionally minimal and beginner-friendly. Each Python file includes TODO comments where you should implement the actual visualizations and analyses.
- Package versions are left unpinned so pip will install recent compatible releases.

Good luck — implement the visualizations inside the task folders and replace placeholders with your figures and written explanations.
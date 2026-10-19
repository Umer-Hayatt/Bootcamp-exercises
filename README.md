# Python to AI Bootcamp - Umer Hayatt

Day 1 and Day 2 practice materials for **Umer Hayatt**, adapted from the bootcamp repositories credited in [ATTRIBUTION.md](ATTRIBUTION.md).

## Materials

- [Day 1 practice notebook](day1_practice.ipynb): variables, data types, input conversion, operators, conditionals, loops, strings, collections, functions and an extended Student Marks Analyzer.
- [Day 1 scripts](day-01/): the supporting Python examples and mini-project.
- [Day 2 notebook](day-2/data-analysis.ipynb): NumPy operations, Pandas exploration, filtering and an answered custom Titanic question.
- [Titanic dataset](day-2/titanic.csv) and [column reference](dataset-info.md).

## Run locally

Use Python 3 and install the notebook dependencies:

```sh
python -m pip install -r requirements.txt
python -m jupyter notebook
```

Open either notebook and run the cells in order. Day 1 asks for a number, price and marks. Its saved example run uses 5, 100 and 85. Other ages, grades and marks are illustrative values.

The Day 2 notebook finds the included CSV from the repository root or the day-2 folder. In Google Colab, it falls back to the CSV in this repository. Each notebook also includes an Open in Colab link.

Run the mini-project separately with:

```sh
python day-01/project.py
```

## Source credit

These are adapted practice materials, with participant names personalized for Umer Hayatt. Original examples and the existing custom query retain credit to their sources; this copy does not claim original authorship of the imported work. See [ATTRIBUTION.md](ATTRIBUTION.md) for the exact source revision and changes.

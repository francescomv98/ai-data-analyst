from pathlib import Path
import pytest
import pandas as pd
from src.data_loader import DataLoader

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def test_load_valid_csv():
    """
    Test loading a valid CSV file.
    """

    file_path = DATA_DIR / "sales.csv"

    dataframe = DataLoader.load_csv(file_path)

    assert isinstance(dataframe, pd.DataFrame)
    assert not dataframe.empty

    assert list(dataframe.columns) == [
        "Date",
        "Product",
        "Region",
        "Revenue"
    ]

def test_load_missing_file():
    """
    Test loading a non-existing CSV file.
    """

    file_path = DATA_DIR / "missing.csv"

    with pytest.raises(FileNotFoundError):
        DataLoader.load_csv(file_path)

def test_load_empty_csv():
    """
    Test loading an empty CSV file.
    """

    file_path = DATA_DIR / "sales_empty.csv"

    with pytest.raises(ValueError):
        DataLoader.load_csv(file_path)

def test_load_csv_with_missing_columns():
    """
    Test loading a CSV missing required columns.
    """

    file_path = DATA_DIR / "sales_missing_columns.csv"

    with pytest.raises(ValueError):
        DataLoader.load_csv(file_path)

def test_load_dirty_csv():
    """
    Test loading a CSV containing invalid values.

    Revenue column contains non numeric values.
    """

    file_path = DATA_DIR / "sales_dirty.csv"

    with pytest.raises(ValueError):
        DataLoader.load_csv(file_path)
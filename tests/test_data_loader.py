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
def test_load_csv_with_invalid_dates(tmp_path):
    file_path = tmp_path / "bad_dates.csv"
    file_path.write_text(
        "Date,Product,Region,Revenue\n"
        "2025-01-03,Laptop,North,1500\n"
        "not a date,Mouse,South,200\n"
    )

    with pytest.raises(ValueError, match="Date"):
        DataLoader.load_csv(file_path)

def test_revenue_is_numeric_after_loading():
    dataframe = DataLoader.load_csv(DATA_DIR / "sales.csv")

    assert pd.api.types.is_numeric_dtype(dataframe["Revenue"])

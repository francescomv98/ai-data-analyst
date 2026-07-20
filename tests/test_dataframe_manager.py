import pandas as pd
from src.dataframe_manager import DataFrameManager

def test_average_revenue(sample_dataframe):
    """
    Test average revenue calculation.
    """

    manager = DataFrameManager(sample_dataframe)

    result = manager.get_average_revenue()

    assert result == 910

def test_top_products(sample_dataframe):
    """
    Test top products calculation.
    """

    manager = DataFrameManager(sample_dataframe)

    result = manager.get_top_products()

    assert isinstance(result, pd.DataFrame)

    assert "Product" in result.columns
    assert "Revenue" in result.columns

    assert result.iloc[0]["Product"] == "Laptop"

def test_best_region(sample_dataframe):
    """
    Test best region calculation.
    """

    manager = DataFrameManager(sample_dataframe)

    result = manager.get_best_region()

    assert isinstance(result, pd.DataFrame)

    assert result.iloc[0]["Region"] == "North"

def test_monthly_revenue(sample_dataframe):
    """
    Test monthly revenue aggregation.
    """

    manager = DataFrameManager(sample_dataframe)

    result = manager.get_monthly_revenue()

    assert isinstance(result, pd.DataFrame)

    assert "Month" in result.columns
    assert "Revenue" in result.columns

    assert len(result) == 3
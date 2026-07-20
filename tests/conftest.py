import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")

@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """
    Provides a valid DataFrame for testing.
    """

    return pd.DataFrame(
        {
            "Date": [
                "2025-01-01",
                "2025-01-15",
                "2025-02-01",
                "2025-02-15",
                "2025-03-01"
            ],
            "Product": [
                "Laptop",
                "Mouse",
                "Laptop",
                "Keyboard",
                "Monitor"
            ],
            "Region": [
                "North",
                "South",
                "North",
                "West",
                "East"
            ],
            "Revenue": [
                1500,
                200,
                1700,
                350,
                800
            ]
        }
    )
import pandas as pd
from src.utils.logger import logger

class DataFrameManager:
    """
    Provides data analysis operations on a pandas DataFrame.
    """

    def __init__(self, dataframe: pd.DataFrame) -> None:
        """
        Initialize the DataFrame manager.

        Args:
            dataframe: The DataFrame to analyze.
        """
        self.df = dataframe.copy()

    def _validate_columns(self, required_columns: list[str]) -> None:
        """
        Validate that all required columns exist.

        Args:
            required_columns: List of required column names.

        Raises:
            ValueError: If one or more columns are missing.
        """
        missing_columns = [column for column in required_columns if column not in self.df.columns]

        if missing_columns:
            logger.error(f"Missing required columns: {missing_columns}")
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    def get_average_revenue(self) -> float:
        """
        Calculate the average revenue.

        Returns:
            Average revenue.
        """
        self._validate_columns(["Revenue"])

        logger.info("Calculating average revenue.")

        average = self.df["Revenue"].mean()

        return float(average)

    def get_top_products(self, top_n: int = 5) -> pd.DataFrame:
        """
        Return the top N products by total revenue.

        Args:
            top_n: Number of products to return.

        Returns:
            DataFrame containing the top products.
        """
        self._validate_columns(["Product", "Revenue"])

        logger.info(f"Calculating top {top_n} products.")

        result = (
            self.df
            .groupby("Product", as_index=False)["Revenue"]
            .sum()
            .sort_values(by="Revenue", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )

        return result

    def get_best_region(self) -> pd.DataFrame:
        """
        Return regions ordered by total revenue.

        Returns:
            DataFrame ordered by revenue.
        """
        self._validate_columns(["Region", "Revenue"])

        logger.info("Calculating revenue by region.")

        result = (
            self.df
            .groupby("Region", as_index=False)["Revenue"]
            .sum()
            .sort_values(by="Revenue", ascending=False)
            .reset_index(drop=True)
        )

        return result

    def get_monthly_revenue(self) -> pd.DataFrame:
        """
        Aggregate revenue by month.

        Returns:
            DataFrame with monthly revenue.
        """
        self._validate_columns(["Date", "Revenue"])

        logger.info("Calculating monthly revenue.")

        dataframe = self.df.copy()

        dataframe["Date"] = pd.to_datetime(dataframe["Date"])

        dataframe["Month"] = (
            dataframe["Date"]
            .dt.to_period("M")
            .astype(str)
        )

        result = (
            dataframe
            .groupby("Month", as_index=False)["Revenue"]
            .sum()
            .sort_values(by="Month")
            .reset_index(drop=True)
        )

        return result
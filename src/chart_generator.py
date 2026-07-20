import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from src.utils.logger import logger

class ChartGenerator:
    """
    Generates charts from processed data.
    """

    @staticmethod
    def plot_monthly_revenue(dataframe: pd.DataFrame) -> Figure:
        """
        Generate a line chart showing monthly revenue.

        Args:
            dataframe: DataFrame containing 'Month' and 'Revenue'.

        Returns:
            A Matplotlib Figure.
        """

        logger.info("Generating monthly revenue chart.")

        required_columns = {"Month", "Revenue"}

        if not required_columns.issubset(dataframe.columns):
            logger.error("Missing required columns for chart generation.")
            raise ValueError("The DataFrame must contain 'Month' and 'Revenue' columns.")

        fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)

        ax.plot(
            dataframe["Month"],
            dataframe["Revenue"],
            marker="o",
            linewidth=2
        )

        ax.set_title("Monthly Revenue")
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.grid(axis="y", linestyle="--", alpha=0.4)

        logger.info("Chart generated successfully.")

        return fig
    
    @staticmethod
    def plot_top_products(dataframe: pd.DataFrame) -> Figure:
        """
        Generate a bar chart of the top products.
        """

        logger.info("Generating top products chart.")

        required_columns = {"Product", "Revenue"}

        if not required_columns.issubset(dataframe.columns):
            logger.error("Missing required columns for chart generation.")
            raise ValueError("The DataFrame must contain 'Product' and 'Revenue' columns.")
        
        fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)

        ax.bar(
            dataframe["Product"],
            dataframe["Revenue"]
        )

        ax.set_title("Top Products")
        ax.set_xlabel("Product")
        ax.set_ylabel("Revenue")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.grid(axis="y", linestyle="--", alpha=0.4)

        logger.info("Chart generated successfully.")

        return fig
    
    @staticmethod
    def plot_best_region(dataframe: pd.DataFrame) -> Figure:
        """
        Generate a bar chart of revenue by region.
        """

        logger.info("Generating region chart.")

        required_columns = {"Region", "Revenue"}

        if not required_columns.issubset(dataframe.columns):
            logger.error("Missing required columns for chart generation.")
            raise ValueError("The DataFrame must contain 'Region' and 'Revenue' columns.")
        
        fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)

        ax.bar(
            dataframe["Region"],
            dataframe["Revenue"]
        )

        ax.set_title("Revenue by Region")
        ax.set_xlabel("Region")
        ax.set_ylabel("Revenue")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.grid(axis="y", linestyle="--", alpha=0.4)

        logger.info("Chart generated successfully.")

        return fig
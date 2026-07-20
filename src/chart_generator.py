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

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(
            dataframe["Month"],
            dataframe["Revenue"],
            marker="o",
            linewidth=2,
        )

        ax.set_title("Monthly Revenue")
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue")

        ax.grid(True)

        fig.tight_layout()

        logger.info("Chart generated successfully.")

        return fig
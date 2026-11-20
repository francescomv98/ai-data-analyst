import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from src.utils.logger import logger

class ChartGenerator:
    """
    Generates charts from processed data.

    Figures are built with the object-oriented API instead of pyplot: pyplot keeps
    every figure alive until it is closed, and it isn't safe to use from the worker
    threads Gradio runs the callbacks in.
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

        ChartGenerator._check_columns(dataframe, "Month", "Revenue")

        fig, ax = ChartGenerator._new_chart()

        ax.plot(
            dataframe["Month"],
            dataframe["Revenue"],
            marker="o",
            linewidth=2
        )

        ChartGenerator._style(ax, "Monthly Revenue", "Month")

        logger.info("Chart generated successfully.")

        return fig

    @staticmethod
    def plot_top_products(dataframe: pd.DataFrame) -> Figure:
        """
        Generate a bar chart of the top products.
        """

        logger.info("Generating top products chart.")

        ChartGenerator._check_columns(dataframe, "Product", "Revenue")

        fig, ax = ChartGenerator._new_chart()

        ax.bar(
            dataframe["Product"].astype(str),
            dataframe["Revenue"]
        )

        ChartGenerator._style(ax, "Top Products", "Product")

        logger.info("Chart generated successfully.")

        return fig

    @staticmethod
    def plot_best_region(dataframe: pd.DataFrame) -> Figure:
        """
        Generate a bar chart of revenue by region.
        """

        logger.info("Generating region chart.")

        ChartGenerator._check_columns(dataframe, "Region", "Revenue")

        fig, ax = ChartGenerator._new_chart()

        ax.bar(
            dataframe["Region"].astype(str),
            dataframe["Revenue"]
        )

        ChartGenerator._style(ax, "Revenue by Region", "Region")

        logger.info("Chart generated successfully.")

        return fig

    @staticmethod
    def _check_columns(dataframe: pd.DataFrame, *columns: str) -> None:
        missing = [column for column in columns if column not in dataframe.columns]

        if missing:
            logger.error("Missing required columns for chart generation.")
            names = " and ".join(f"'{column}'" for column in columns)
            raise ValueError(f"The DataFrame must contain {names} columns.")

    @staticmethod
    def _new_chart() -> tuple[Figure, Axes]:
        fig = Figure(figsize=(8, 5), constrained_layout=True)
        ax = fig.subplots()
        return fig, ax

    @staticmethod
    def _style(ax: Axes, title: str, x_label: str) -> None:
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel("Revenue")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.grid(axis="y", linestyle="--", alpha=0.4)

        # long product names / many months overlap otherwise
        ax.tick_params(axis="x", labelrotation=30)

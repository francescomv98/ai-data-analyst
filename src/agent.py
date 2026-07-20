import pandas as pd
from src.chart_generator import ChartGenerator
from src.dataframe_manager import DataFrameManager
from src.llm.openai_client import OpenAIClient
from src.utils.logger import logger

class Agent:
    """
    Orchestrates the interaction between the LLM and the data analysis tools.
    """

    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.manager = DataFrameManager(dataframe)
        self.llm = OpenAIClient()

        self.actions = {
            "average_revenue": self._average_revenue,
            "top_products": self._top_products,
            "best_region": self._best_region,
            "monthly_revenue": self._monthly_revenue
        }

    def process_request(self, user_request: str) -> dict:
        """
        Process a user request.

        Args:
            user_request: User question.

        Returns:
            Dictionary containing the response.
        """

        logger.info("Processing user request.")

        action = self.llm.detect_action(user_request)

        if action not in self.actions:
            logger.warning(f"Unsupported action: {action}")

            return {
                "message": "Sorry, I couldn't understand your request.",
                "table": None,
                "chart": None
            }

        return self.actions[action]()

    def _average_revenue(self) -> dict:

        average = self.manager.get_average_revenue()

        return {
            "message": f"Average revenue: {average:.2f}",
            "table": None,
            "chart": None
        }

    def _top_products(self) -> dict:

        dataframe = self.manager.get_top_products()

        figure = ChartGenerator.plot_top_products(dataframe)

        return {
            "message": "Top products by revenue.",
            "table": dataframe,
            "chart": figure
        }

    def _best_region(self) -> dict:

        dataframe = self.manager.get_best_region()

        figure = ChartGenerator.plot_best_region(dataframe)

        return {
            "message": "Regions ranked by revenue.",
            "table": dataframe,
            "chart": figure
        }

    def _monthly_revenue(self) -> dict:

        dataframe = self.manager.get_monthly_revenue()

        figure = ChartGenerator.plot_monthly_revenue(dataframe)

        return {
            "message": "Monthly revenue.",
            "table": dataframe,
            "chart": figure
        }
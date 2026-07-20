from openai import OpenAI
from src.config.settings import settings
from src.utils.logger import logger

class OpenAIClient:
    """
    Wrapper around the OpenAI API used to classify user requests.
    """

    VALID_ACTIONS = {
        "average_revenue",
        "top_products",
        "best_region",
        "monthly_revenue",
        "unknown"
    }

    def __init__(self) -> None:
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.chat_model

    def detect_action(self, user_request: str) -> str:
        """
        Detect which analysis action should be executed.

        Args:
            user_request: User natural language question.

        Returns:
            One of the supported actions.
        """

        logger.info("Sending request to OpenAI.")

        system_prompt = """
You are an AI assistant that classifies data analysis requests.

Return ONLY one of these values:

average_revenue
top_products
best_region
monthly_revenue
unknown

Rules:

- "average sales"
- "average revenue"
- "mean revenue"
-> average_revenue

- "top products"
- "best selling products"
- "highest revenue products"
-> top_products

- "best region"
- "highest revenue region"
- "top region"
-> best_region

- "monthly revenue"
- "plot monthly revenue"
- "monthly sales"
- "revenue over time"
-> monthly_revenue

If you are not sure:

unknown

Return only the action.
"""

        try:
            response = self.client.responses.create(
                model=self.model,
                input=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_request
                    }
                ]
            )

            action = response.output_text.strip()

            logger.info(f"Detected action: {action}")

            if action not in self.VALID_ACTIONS:
                logger.warning("Invalid action returned by OpenAI.")
                return "unknown"

            return action

        except Exception as e:
            logger.error(f"OpenAI request failed: {e}")
            raise RuntimeError("Failed to classify the user request.")
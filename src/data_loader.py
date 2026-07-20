from pathlib import Path
import pandas as pd
from src.utils.logger import logger

class DataLoader:
    """Handles loading CSV files into pandas DataFrames."""

    @staticmethod
    def load_csv(file_path: str | Path) -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.

        Args:
            file_path: Path to the CSV file.

        Returns:
            A pandas DataFrame.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the CSV is empty.
            RuntimeError: If the CSV cannot be loaded.
        """

        file_path = Path(file_path)

        logger.info(f"Loading CSV file: {file_path}")

        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        try:
            dataframe = pd.read_csv(file_path)

            if dataframe.empty:
                logger.error("The uploaded CSV is empty.")
                raise ValueError("The uploaded CSV is empty.")

            logger.info(f"CSV loaded successfully ({len(dataframe)} rows, {len(dataframe.columns)} columns).")

            return dataframe

        except pd.errors.EmptyDataError:
            logger.error("CSV file contains no data.")
            raise ValueError("CSV file contains no data.")

        except Exception as e:
            logger.error(f"Unexpected error while loading CSV: {e}")
            raise RuntimeError("Unable to load the CSV file.") from e
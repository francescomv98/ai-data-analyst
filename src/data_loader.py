from pathlib import Path
import pandas as pd
from src.utils.logger import logger

class DataLoader:
    """Handles loading CSV files into pandas DataFrames."""

    REQUIRED_COLUMNS = [
        "Date",
        "Product",
        "Region",
        "Revenue"
    ]

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
            ValueError: If the CSV is invalid.
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

            DataLoader._validate_columns(dataframe)

            DataLoader._validate_data_types(dataframe)

            rows = len(dataframe)
            columns = len(dataframe.columns)

            logger.info(
                f"CSV loaded successfully "
                f"({rows} rows, {columns} columns)."
            )

            return dataframe
        except pd.errors.EmptyDataError:
            logger.error("CSV file contains no data.")
            raise ValueError("CSV file contains no data.")
        except (FileNotFoundError, ValueError):
            raise
        except Exception:
            logger.exception("Unexpected error while loading CSV.")
            raise RuntimeError("Unable to load the CSV file.")

    @staticmethod
    def _validate_columns(dataframe: pd.DataFrame) -> None:
        """
        Validate required CSV columns.
        """

        missing_columns = [column for column in DataLoader.REQUIRED_COLUMNS if column not in dataframe.columns]

        if missing_columns:
            logger.error(f"Missing columns: {missing_columns}")
            raise ValueError("Missing required columns: " + ", ".join(missing_columns))

    @staticmethod
    def _validate_data_types(dataframe: pd.DataFrame) -> None:
        """
        Validate required column data types.
        """

        invalid_revenue = pd.to_numeric(dataframe["Revenue"], errors="coerce").isna()

        if invalid_revenue.any():

            invalid_count = invalid_revenue.sum()

            logger.error(f"Found {invalid_count} invalid Revenue values.")

            raise ValueError(
                f"Revenue column contains "
                f"{invalid_count} invalid values."
            )
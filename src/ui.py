import gradio as gr
import pandas as pd
from src.agent import Agent
from src.data_loader import DataLoader
from src.utils.logger import logger

def upload_csv(file_path: str | None) -> tuple[pd.DataFrame | None, str]:
    """
    Load the uploaded CSV file.

    Args:
        file_path: Path of the file uploaded through Gradio.

    Returns:
        The loaded DataFrame (or None) and a status message for the user.
    """

    if not file_path:
        logger.warning("No CSV file uploaded.")
        return None, ""

    try:
        dataframe = DataLoader.load_csv(file_path)
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Failed to load CSV: {e}")
        return None, f"Could not load the file: {e}"
    except Exception as e:
        logger.error(f"Failed to load CSV: {e}")
        return None, "Could not load the file."

    logger.info("CSV uploaded successfully.")

    return dataframe, f"File loaded: {len(dataframe)} rows."


def analyze_request(dataframe: pd.DataFrame | None, question: str):
    """
    Analyze the user request.

    Returns:
        message, table, chart
    """

    if dataframe is None:
        return (
            "Please upload a CSV file first.",
            None,
            None
        )

    if not question or not question.strip():
        return (
            "Please enter a question.",
            None,
            None
        )

    try:
        agent = Agent(dataframe)

        result = agent.process_request(question)

        return (
            result["message"],
            result["table"],
            result["chart"]
        )
    except ValueError as e:
        # data problems (e.g. bad dates) are worth showing to the user as they are
        logger.error(f"Request processing failed: {e}")

        return (
            str(e),
            None,
            None
        )
    except Exception as e:
        logger.error(f"Request processing failed: {e}")

        return (
            "An unexpected error occurred.",
            None,
            None
        )


def create_interface() -> gr.Blocks:

    with gr.Blocks(title="AI Data Analyst") as demo:

        gr.Markdown(
            """
            # AI Data Analyst

            Upload a CSV file and ask questions in natural language.
            """
        )

        dataframe_state = gr.State()

        with gr.Row():
            file_input = gr.File(label="Upload CSV", file_types=[".csv"], type="filepath")

        upload_status = gr.Markdown()

        question = gr.Textbox(label="Question", placeholder="Example: Show the top 5 products")

        gr.Examples(
            examples=[
                ["Show the top 5 products"],
                ["What is the average revenue?"],
                ["Which region performs best?"],
                ["Plot monthly revenue"]
            ],
            inputs=question
        )

        analyze_button = gr.Button("Analyze", variant="primary")

        message = gr.Textbox(label="Answer", interactive=False)

        table = gr.Dataframe(label="Table", interactive=False)

        chart = gr.Plot(label="Chart")

        file_input.upload(
            fn=upload_csv,
            inputs=file_input,
            outputs=[dataframe_state, upload_status]
        )

        # removing the file must also forget the old data
        file_input.clear(
            fn=lambda: (None, ""),
            outputs=[dataframe_state, upload_status]
        )

        analyze_button.click(
            fn=analyze_request,
            inputs=[
                dataframe_state,
                question
            ],
            outputs=[
                message,
                table,
                chart
            ]
        )

        question.submit(
            fn=analyze_request,
            inputs=[dataframe_state, question],
            outputs=[message, table, chart]
        )

    return demo
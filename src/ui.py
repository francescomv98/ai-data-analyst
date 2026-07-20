import gradio as gr
import pandas as pd
from src.agent import Agent
from src.data_loader import DataLoader
from src.utils.logger import logger

def upload_csv(file) -> pd.DataFrame | None:
    """
    Load the uploaded CSV file.

    Args:
        file: Uploaded file from Gradio.

    Returns:
        Loaded DataFrame or None.
    """

    if file is None:
        logger.warning("No CSV file uploaded.")
        return None

    try:
        dataframe = DataLoader.load_csv(file.name)

        logger.info("CSV uploaded successfully.")

        return dataframe
    except Exception as e:
        logger.error(f"Failed to load CSV: {e}")
        return None


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

    if not question.strip():
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
            file_input = gr.File(label="Upload CSV", file_types=[".csv"])

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
            outputs=dataframe_state
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

    return demo
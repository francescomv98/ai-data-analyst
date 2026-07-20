# AI Data Analyst Agent

An AI-powered data analysis assistant built with Python, Gradio, Pandas and OpenAI.

The application allows users to upload CSV files and interact with an AI agent capable of understanding natural language requests, performing data analysis operations and generating visual insights.

Users can ask questions such as:
- What are the top 5 products?
- Show average revenue.
- Which region performs best?
- Plot monthly revenue.

The goal of this project is to demonstrate the implementation of an AI agent workflow combining LLM-based intent detection, data processing, visualization generation and a user-friendly Gradio interface.

---

## Features

- CSV file upload through Gradio interface
- Natural language data analysis requests
- OpenAI-powered request classification
- Automated Pandas data analysis
- Revenue calculations
- Product ranking analysis
- Regional performance analysis
- Monthly revenue aggregation
- Automatic chart generation with Matplotlib
- Data validation and error handling
- Structured logging
- Configuration management with Pydantic Settings
- Unit tests with pytest

---

## Architecture

The application follows a modular architecture where each component has a specific responsibility.

```
                         User
                          |
                          v
                  +---------------+
                  |    Gradio     |
                  |  Interface    |
                  +---------------+
                          |
                          v
                  +---------------+
                  |     Agent     |
                  | Orchestrator  |
                  +---------------+
                    |          |
                    |          |
                    v          v

          +---------------+   +---------------+
          | Data Loader   |   | OpenAI Client |
          |               |   | Intent        |
          | CSV Parsing   |   | Detection     |
          +---------------+   +---------------+
                    |
                    v

          +----------------------+
          | DataFrame Manager    |
          |----------------------|
          | - Average revenue    |
          | - Top products       |
          | - Best region        |
          | - Monthly revenue    |
          +----------------------+

                    |
                    v

          +----------------------+
          | Chart Generator      |
          |----------------------|
          | - Matplotlib charts  |
          | - Data visualization |
          +----------------------+
```

---

## How it works

The workflow follows these steps:
1. The user uploads a CSV file through the Gradio interface.
2. The file is loaded and validated.
3. The user sends a natural language request.
4. The request is analyzed by the OpenAI client.
5. The LLM classifies the requested operation.
6. The Agent executes the corresponding Pandas analysis.
7. If required, Matplotlib generates a visualization.
8. The result is returned to the user through the Gradio interface.

Example:

```
User:
"Which region performs best?"

        |
        v

OpenAI Intent Detection

        |
        v

best_region

        |
        v

DataFrame Analysis

        |
        v

Result + Visualization
```

---

## Main Components

### Agent

The main orchestrator of the application.

Responsibilities:
- coordinate the workflow;
- manage the interaction between components;
- execute the correct analysis operation.

---

### Data Loader

Responsible for CSV ingestion.

Features:
- file validation;
- required column checking;
- data type validation;
- error handling.

Supported validation cases:
- missing files;
- empty CSV files;
- missing columns;
- invalid numerical values.

---

### OpenAI Client

Wrapper around the OpenAI API.

Responsibilities:
- understand user requests;
- classify the required analysis action;
- return a supported operation.

Supported actions:

```
average_revenue
top_products
best_region
monthly_revenue
unknown
```

---

### DataFrame Manager

Contains the business logic for data analysis.

Implemented operations:
- average revenue calculation;
- top products ranking;
- revenue by region;
- monthly revenue aggregation.

---

### Chart Generator

Responsible for creating visualizations.

Implemented charts:
- monthly revenue trend;
- top products bar chart;
- regional revenue chart.

Charts are generated using Matplotlib and displayed directly in Gradio.

---

## Tech Stack

### Backend / Data Processing

- Python
- Pandas

### AI / LLM

- OpenAI API

### User Interface

- Gradio

### Visualization

- Matplotlib

### Configuration

- Pydantic Settings
- python-dotenv

### Testing

- Pytest

### Development Tools

- Git
- Virtual Environment

---

## Project Structure

```
ai-data-analyst/

│
├── src/
│   │
│   ├── config/
│   │   └── settings.py              # Application configuration
│   │
│   ├── llm/
│   │   └── openai_client.py         # OpenAI wrapper
│   │
│   ├── utils/
│   │   └── logger.py                # Logging configuration
│   │
│   ├── agent.py                     # Agent orchestration
│   ├── data_loader.py               # CSV loading and validation
│   ├── dataframe_manager.py         # Data analysis logic
│   ├── chart_generator.py           # Matplotlib visualization
│   └── ui.py                        # Gradio interface
│
├── tests/
│   │
│   ├── conftest.py                  # Shared test fixtures
│   ├── test_data_loader.py
│   ├── test_dataframe_manager.py
│   ├── test_chart_generator.py
│   └── test_openai_client.py
│
├── data/
│   └── sample CSV files
│
├── .env
├── requirements.txt
├── main.py
└── README.md
```

---

## Installation

### Requirements

- Python 3.11+
- OpenAI API key

---

### Clone the repository

```bash
git clone https://github.com/francescomv98/ai-data-analyst.git

cd ai-data-analyst
```

---

### Create virtual environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
APP_NAME=AI Data Analyst

APP_VERSION=1.0.0

OPENAI_API_KEY=your_openai_api_key

CHAT_MODEL=gpt-4.1-mini
```

The application uses Pydantic Settings to load configuration values.

---

## Running the Application

Start the application:

```bash
python main.py
```

The Gradio interface will be available at:

```
http://localhost:7860
```

---

## Example Usage

Upload a CSV file containing sales information.

Example questions:

```
What are the top 5 products?
```

```
Show average revenue.
```

```
Which region performs best?
```

```
Plot monthly revenue.
```

Example workflow:

```
CSV Upload

        |

User Question

        |

AI Intent Detection

        |

Data Analysis

        |

Table / Chart Output
```

---

## Testing

The project includes unit tests using pytest.

Run:

```bash
pytest
```

Covered components:
- CSV loading and validation
- Data analysis operations
- Chart generation
- OpenAI client behavior
- Error handling

---

## Error Handling and Logging

The application includes:
- validation of uploaded files;
- controlled exception handling;
- logging of important execution steps.

Examples of logged events:
- CSV loading;
- analysis execution;
- OpenAI requests;
- generated results;
- unexpected failures.
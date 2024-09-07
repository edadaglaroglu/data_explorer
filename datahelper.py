import pandas as pd
from langchain_experimental.agents.agent_toolkits.pandas.base import (
    create_pandas_dataframe_agent,
)
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


# .env dosyasını yükleyin
load_dotenv()
my_key_openai = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM
llm_gpt = ChatOpenAI(api_key=my_key_openai, model="gpt-4", temperature=0)  # Model ismini doğru şekilde güncelledim
selected_llm = llm_gpt

# Function to summarize the data from a CSV file
def summarize_csv(data_file):
    df = pd.read_csv(data_file, low_memory=False)

    # Create a pandas dataframe agent
    pandas_agent = create_pandas_dataframe_agent(
        selected_llm,
        df,
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": "True"},
        allow_dangerous_code=True  # allow_dangerous_code ekledim
    )

    data_summary = {}

    # Initial data sample (first few rows)
    data_summary["initial_data_sample"] = df.head()

    # Create a table of column descriptions in English
    data_summary["column_descriptions"] = pandas_agent.run("Create a table that includes the column names and a brief description of the information they contain. Provide the response in table format.")

    # Check for missing values in the dataset
    data_summary["missing_values"] = pandas_agent.run("Are there any missing values in this dataset? If so, how many? Respond in the format 'There are X cells with missing data in this dataset.'")

    # Check for duplicate values in the dataset
    data_summary["duplicate_values"] = pandas_agent.run("Are there any duplicate values in this dataset? If so, how many? Respond in the format 'There are X duplicate values in this dataset.'")

    # Summary of essential metrics
    data_summary["essential_metrics"] = df.describe()

    return data_summary


# Function to load the dataframe from a CSV file
def get_dataframe(data_file):
    df = pd.read_csv(data_file, low_memory=False)
    return df


# Function to analyze the trend of a specific variable in the dataset
def analyze_trend(data_file, variable_of_interest):
    df = pd.read_csv(data_file, low_memory=False)

    # Create a pandas dataframe agent
    pandas_agent = create_pandas_dataframe_agent(
        selected_llm,
        df,
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": "True"},
        allow_dangerous_code=True  # allow_dangerous_code ekledim
    )

    # Analyze the trend for the selected variable
    trend_response = pandas_agent.run(f"Briefly comment on the trend of the following variable in the dataset: {variable_of_interest}. Since the dataset is time-based from past to present, use the rows to help your interpretation. Provide the answer in English.")

    return trend_response


# Function to ask a specific question about the dataset
def ask_question(data_file, question):
    df = pd.read_csv(data_file, low_memory=False)

    # Create a pandas dataframe agent
    pandas_agent = create_pandas_dataframe_agent(
        selected_llm,
        df,
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": "True"},
        allow_dangerous_code=True  # allow_dangerous_code ekledim
    )

    # Ask a specific question and get an answer from the AI
    AI_Response = pandas_agent.run(f"{question} Provide the answer in English.")

    return AI_Response

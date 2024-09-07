Data Explorer: Natural Language Data Exploration with Pandas and OpenAI 🤖

This project is a Streamlit application designed for exploring CSV files through natural language interaction, powered by OpenAI's GPT-4 model. A key feature of this project is the use of LangChain's Pandas DataFrame Agent, which processes data dynamically using natural language commands instead of traditional Pandas operations.

#Features

CSV File Upload: Easily upload a CSV file through the web interface.
Data Summary: Automatically generates a summary of the dataset, including:
-Sample data
-Missing values
-Duplicate data
-Basic statistics
Variable Trend Analysis: Visualize the trends of selected variables with an interactive line chart.
Natural Language Interaction: Ask questions about the dataset in natural language and receive insights powered by OpenAI GPT-4, assisted by the Pandas DataFrame Agent.


#Files

1. datahelper.py
This script contains the core logic for:
-Summarizing the dataset
-Analyzing trends
-Answering user queries
-It uses a Pandas DataFrame Agent to process the data via natural language commands instead of direct Pandas operations.

#Functions:

@summarize_csv():
Provides a sample of the data.
Describes columns.
Detects missing and duplicate values using the Pandas DataFrame Agent.
@get_dataframe():
Loads the CSV file into a Pandas DataFrame.
@analyze_trend():
Uses the Pandas DataFrame Agent to analyze trends in a selected variable.
@ask_question():
Allows users to ask custom questions about the dataset, with responses generated through GPT-4 and the Pandas DataFrame Agent.

2. app.py
This is the front-end of the application, built using Streamlit. It handles the user interface, file uploads, and calls the functions from datahelper.py to generate insights.

Layout:

Sidebar: For uploading the CSV file.
Data Summary Section: Displays:
-Sample data
-Missing values
-Duplicate data
-Basic metrics
-Data Interaction Section: Allows users to:
-Select a variable for trend analysis
-Ask natural language questions about the data


#Pandas DataFrame Agent

Instead of using traditional Pandas operations directly, this application utilizes a Pandas DataFrame Agent from the LangChain framework. The agent processes data using natural language prompts, making data exploration flexible and interactive without the need for writing Pandas code.

The Pandas DataFrame Agent can:

Generate data summaries.
Detect missing or duplicate data.
Provide insights on variables and trends.
Answer specific user questions about the dataset in natural language.
The agent is integrated with OpenAI's GPT-4, which helps interpret and generate meaningful responses to user queries.

#Requirements

To run the application, you need the following:

Python Packages
LangChain: For integrating with OpenAI's GPT-4 model and using the Pandas DataFrame Agent.
Streamlit: For building the web interface.
Pandas: For data processing and manipulation.
dotenv: For loading environment variables.

#Conclusion

This project demonstrates how to integrate natural language processing with data exploration using OpenAI's GPT-4 and LangChain's Pandas DataFrame Agent. By utilizing the agent, users can interact with datasets in a conversational manner, making it easier to derive insights without writing complex code.

Feel free to explore the dataset and interact with it using natural language! 🚀

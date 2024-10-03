# AI Assistant

This project is an AI Assistant built using LangChain and Llama3.1. The assistant helps users plan events like birthday parties by gathering information about venues, caterers, and entertainment options.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Project Locally with Docker](#setup-project-locally-with-docker)
- [Run Locally Without Docker](#run-locally-without-docker)
- [View Live on Streamlit](#view-live-on-streamlit)

## Project Overview

Imagine you're designing a smart assistant to help someone plan a birthday party. This assistant isn't just a search engine—it needs to act on behalf of the user to get things done. The user provides details about the party they want to throw, and the assistant recommends and books the best options, explaining its choices along the way.

## Technologies Used

- **LangChain**: Framework for building AI applications.
- **Groq API**: For natural language processing.
- **Streamlit**: For creating a web interface.
- **Docker**: For containerization.

## Setup Project Locally with Docker

To set up the project using Docker, follow these instructions:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/remon-rakibul/birthday-planner-ai-agent.git
   cd birthday-planner-ai-agent
   ```

2. **Build Docker Image Locally:**
   Build the Docker image with the following command:
   ```bash
   docker build -t ai_assistant:latest .
   ```
   Alternatively, you can pull the image from Docker Hub:
   ```bash
   docker pull remon007/ai_assistant
   ```

3. **Run Docker Container:**
   Start the Docker container with the following command:
   ```bash
   docker run -it --rm -p 8501:8501 ai_assistant:latest
   ```

4. **Access the Application:**
   Open your browser and go to the following URL:
   ```
   http://localhost:8501
   ```

## Run Locally Without Docker

If you prefer to run the application without Docker, you can do so by following these steps:

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**
   For macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   For Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install Requirements:**
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Locally with Streamlit UI:**
   To start the Streamlit UI, use the following command:
   ```bash
   streamlit run frontend.py
   ```

5. **Run the Agent in Terminal:**
   You can also run the agent directly from the terminal:
   ```bash
   python agent.py
   ```

## View Live on Streamlit

You can view the live application at the following URL:

Live URL: 

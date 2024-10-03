# Use an official Python runtime as a parent image
FROM python:3.12.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your application runs on (if applicable)
EXPOSE 8501



# Run the application
CMD ["streamlit", "run", "frontend.py"]

# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt alone into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Copy the current directory contents into the container at /app
COPY . /app/

# Run the command to start the Streamlit app
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]

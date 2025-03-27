# Use an official Python 3.9 image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port of the app
EXPOSE 8000

# Define the command to run your app
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "run.py"]

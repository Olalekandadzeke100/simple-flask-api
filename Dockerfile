# Use a base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Run the app
CMD ["python", "app.py"]


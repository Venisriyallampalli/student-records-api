# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency definition
COPY requirements.txt .

# Install dependencies without cache to keep image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variable to run in production mode
ENV FLASK_ENV=production

# Run the Flask application
CMD ["python", "app.py"]

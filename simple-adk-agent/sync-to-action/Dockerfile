FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV PORT=8080
# Cloud Run needs the app to listen on 0.0.0.0
ENV HOST=0.0.0.0

# Expose port 8080
EXPOSE 8080

# CHANGE THIS: Run the script directly instead of using uvicorn command
CMD ["python", "agent.py"]
FROM python:3.8

# Ser working directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt requirements.txt

# Copy the current directory contents into the container at /app
COPY . ./app/

# Start the server
CMD ["uvicorn", "app.main:app", "--reload", "--workers", "4", "--worker-class", \
    "uvicorn.workers.UvicornWorker", "--host", "0.0.0.0", "--port", "8000"]
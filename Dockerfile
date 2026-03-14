# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app


# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run migrations
RUN python manage.py migrate

# Expose port
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

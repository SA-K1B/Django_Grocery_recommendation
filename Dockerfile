FROM python:3.11.10-slim

# Set the working directory
WORKDIR /django

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY ./ .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose a default port (optional, for documentation purposes)
EXPOSE ${PORT}

# Start the application using Gunicorn, using the PORT environment variable
CMD ["sh", "-c", "gunicorn groceryRecommendation.wsgi:application --bind 0.0.0.0:${PORT:-3000}"]

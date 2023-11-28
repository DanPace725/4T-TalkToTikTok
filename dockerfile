# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update

# Install ffmpeg for audio conversion
RUN apt-get install -y ffmpeg

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code
COPY . /code/

# Collect static files
RUN python django/manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django.T2TT.wsgi:application"]

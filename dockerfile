# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH

RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y curl gnupg dbus

# Install Google Chrome
RUN curl --location --silent https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
 && apt-get update \
 && apt-get install google-chrome-stable -y --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

# Install ffmpeg for audio conversion
RUN apt-get update && apt-get install -y ffmpeg

# Create the system bus socket
RUN mkdir -p /run/dbus && touch /run/dbus/system_bus_socket


# Set the DBUS_SESSION_BUS_ADDRESS environment variable
ENV DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus


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

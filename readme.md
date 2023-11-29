## Overview

This Django project is a web application that enables users to upload videos for transcription using an AI service. Users can download the resulting transcriptions in a variety of formats.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

#### Environment

To set up the application, ensure Docker and Docker Compose are installed on your system. Docker containers will encapsulate the application and its services, while Docker Compose orchestrates the containers.

Create a `.env` file in the project root with the following content:

```
DEBUG=1
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

#### Running the Application

1. Build the Docker image:
   `docker-compose build`
2. Start the services:
   `docker-compose up`
3. Access the application at http://localhost:8000.
4. To stop and remove the containers:
   `docker-compose down`

#### Database

The application uses PostgreSQL, which is defined in the `docker-compose.yml` file. Use environment variables to override the default configurations.

#### Static Files

Collect static files in the `staticfiles` directory with:
`docker-compose run web python manage.py collectstatic`

#### Migrations

Apply database migrations with:
`docker-compose run web python manage.py migrate`

#### Admin Interface

Create a superuser to access the Django admin at http://localhost:8000/admin:
`docker-compose run web python manage.py createsuperuser`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Docker Hub for the official Python Docker image.
- PostgreSQL for the database image.

Refer to the project repository for more details on structure and configurations.

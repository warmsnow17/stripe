# Use an official Python runtime as the base image
FROM python:3

# Set the working directory to /app
RUN mkdir /djangosite

# Copy the lockfile and pyproject.toml
COPY poetry.lock pyproject.toml /

# Install Poetry and dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copy the application code
COPY ./ /djangosite

# Collect the static files
WORKDIR /djangosite/app
# RUN python manage.py collectstatic --noinput
#RUN python manage.py makemigrations
#RUN python manage.py migrate

# Expose port 8000 for Daphne to listen on
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

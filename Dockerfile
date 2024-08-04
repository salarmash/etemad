# Use an official Python runtime as a parent image
FROM python

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /code
COPY requirments.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirments.txt

# Copy the current directory contents into the container at /code
COPY . /app/

EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Dockerfile is a text file with instructions on how to build the docker image.
# It's a blueprint for the image, scpecifying the environment, app and dependencies.

# FROM - Specifies the base image
# Use an official Python runtime as a parent image
FROM python-3.8

# Set the working directory contents into the container at /app
WORKDIR /app

# COPY or ADD - Adds files from your boot system into image.
COPY . /app

# RUN - Executes commands in the image, such as installing Software
# Install any needed packages specified in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE - Specifies the port the container will  liston on.
# Make a port 5000 available to the world outside this container
EXPOSE 5000

# CMD or ENTRYPOINT - Defines the command that runs when the container starts.
# Define environment variable
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
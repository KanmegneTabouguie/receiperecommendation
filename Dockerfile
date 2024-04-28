# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the content of the backend directory into the container at /app

#COPY app.py /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask scikit-learn gunicorn

# Make port 5033 available to the world outside this container
EXPOSE 5033

# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:5033", "app:app"]

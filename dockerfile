
# Use a Python base image
FROM python:3.8

# Set the working directory
WORKDIR /myapitest

# Copy the application files to the container
COPY myapitest.py /myapitest


# Install dependencies
RUN pip install flask
RUN pip install --upgrade pip

# port to expose
EXPOSE 5000

# Run the application
CMD ["python3", "myapitest.py"]

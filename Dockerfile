# Use the official Python image as the base image
FROM python:3.11-slim

# please review all the latest versions here:
# https://googlechromelabs.github.io/chrome-for-testing/
ENV CHROMEDRIVER_VERSION=124.0.6367.78

### install chrome
RUN apt-get update && apt-get install -y wget && apt-get install -y zip
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.78/linux64/chrome-linux64.zip \
    && unzip chrome-linux64.zip && rm -dfr chrome-linux64.zip
#RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN unzip chrome-linux64.zip \

### install chromedriver
    #https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip
RUN wget https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.78/linux64/chromedriver-linux64.zip \
  && unzip chromedriver-linux64.zip && rm -dfr chromedriver_linux64.zip \
  && mv /chromedriver-linux64/chromedriver /usr/bin/chromedriver \
  && chmod +x /usr/bin/chromedriver

RUN apt-get install -y chromium-driver

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . .

# Run the Python script when the container launches
CMD ["python", "main.py"]

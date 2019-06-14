#FROM ubuntu:latest
#MAINTAINER Pankaj Sharma "luvneries@gmail.com"
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#EXPOSE 3000
#ENTRYPOINT ["python"]
#CMD ["main.py"]

# Dockerfile-flask
# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3
# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP
# Expose the port uWSGI will listen on
EXPOSE 3000
# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt
# We copy the rest of the codebase into the image
COPY . .
# Finally, we run uWSGI with the ini file we
# created earlier
CMD [ "uwsgi", "--ini", "wsgi.ini" ]
# Use gunicorn server
#CMD ["gunicorn", "-b", "0.0.0.0:3000", "wsgi:app"]

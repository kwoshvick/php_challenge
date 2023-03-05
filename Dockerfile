# start from an official image
FROM python:3.10.6

ARG app_name='Pbp Challenge'
MAINTAINER Kwoshvick

# Python Domain
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# arbitrary location choice: you can change the directory
RUN mkdir -p /app
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy our project code
COPY . /app
RUN chmod a+x /app/entrypoint.sh
RUN chmod a+x /app/wait-for-it.sh

# define the default command to run when starting the container
ENTRYPOINT ["/app/entrypoint.sh"]

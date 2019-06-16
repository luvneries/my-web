FROM python:3.7
ENV APP /app
RUN mkdir $APP
WORKDIR $APP
EXPOSE 5000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# for uwsgi app server
#CMD [ "uwsgi", "--ini", "wsgi.ini"]
# for gunicorn server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
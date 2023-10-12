FROM python:3.8.5

WORKDIR /app

COPY . .

#RUN pip3 install -r requirements.txt --no-cache-dir
#
#CMD gunicorn english_brake_fast.wsgi:application --bind 0.0.0.0:8000

#CMD python manage.py run_bot
FROM python:3.4

# Make source code directory
RUN mkdir -p /usr/src/app

# Install requirements
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Expose port 8000 by default
EXPOSE 8000

CMD ["gunicorn", "-c", "curd/settings/gunicorn.py", "curd.wsgi:application"]

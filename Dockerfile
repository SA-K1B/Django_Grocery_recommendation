FROM python:3.11.10-slim
WORKDIR /django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
RUN python manage.py collectstatic --noinput
EXPOSE 3000
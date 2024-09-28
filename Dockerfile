FROM python:3.11.10-slim

WORKDIR /django

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ .

RUN python manage.py collectstatic --noinput

EXPOSE ${PORT}

CMD ["sh", "-c", "gunicorn groceryRecommendation.wsgi:application --bind 0.0.0.0:${PORT:-3000}"]

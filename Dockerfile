FROM python:3.11.10-slim
WORKDIR /django
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
EXPOSE 3000
CMD [ "python","manage.py","runserver","0.0.0.0:3000" ]
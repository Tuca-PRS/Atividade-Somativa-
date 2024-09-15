FROM python:3.12

WORKDIR app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HTTP_HOST=0.0.0.0
ENV HTTP_PORT=8000
ENV ALLOWED_HOSTS=*

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver ${HTTP_HOST}:${HTTP_PORT}"]

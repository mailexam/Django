import json
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-mailexam-example-only",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "mailapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MAILEXAM_LOGIN = os.environ.get("MAILEXAM_LOGIN", "")
MAILEXAM_PASSWORD = os.environ.get("MAILEXAM_PASSWORD", "")
MAILEXAM_PORT = int(os.environ.get("MAILEXAM_PORT", "587"))

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = f"{MAILEXAM_LOGIN}.mailexam.io" if MAILEXAM_LOGIN else "localhost"
EMAIL_PORT = MAILEXAM_PORT
EMAIL_USE_TLS = MAILEXAM_PORT in (587, 2525)
EMAIL_HOST_USER = MAILEXAM_LOGIN
EMAIL_HOST_PASSWORD = MAILEXAM_PASSWORD
DEFAULT_FROM_EMAIL = os.environ.get("MAIL_FROM", "noreply@example.test")

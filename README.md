# Django + Mailexam

Minimal [Django](https://www.djangoproject.com/) example that sends test mail through [Mailexam](https://mailexam.ru/) SMTP via `django.core.mail`.

Based on the [Mailexam Django guide](https://wiki.mailexam.ru/en/examples/django/).

## What you need

- A Mailexam account and a project with SMTP credentials.
- Python 3.10+ and pip.

From your Mailexam welcome email or dashboard:

| Variable | Description |
|----------|-------------|
| `MAILEXAM_LOGIN` | SMTP login (for example, `xxxxx`) |
| `MAILEXAM_PASSWORD` | SMTP password (paired with the login) |
| Host | `{MAILEXAM_LOGIN}.mailexam.ru` (built in `config/settings.py`) |

## Quick start (host)

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy the example environment file and fill in your credentials:

```bash
cp .env.example .env
```

3. Edit `.env`:

```env
MAILEXAM_LOGIN=YOUR_LOGIN
MAILEXAM_PASSWORD=YOUR_PASSWORD
MAILEXAM_PORT=587
MAIL_FROM=noreply@example.test
```

4. Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

The server listens on `http://127.0.0.1:8000` by default.

5. Send a test message:

```bash
curl -X POST http://127.0.0.1:8000/mail/test \
  -H 'Content-Type: application/json' \
  -d '{"to":"user@example.test","subject":"Test","body":"Hello"}'
```

The message appears in the Mailexam dashboard → your project → inbox.

### Django shell alternative

```bash
python manage.py shell
```

```python
from django.core.mail import send_mail

send_mail(
    "Django + Mailexam",
    "Mailexam test from Django",
    None,
    ["user@example.test"],
)
```

## Environment variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `MAILEXAM_LOGIN` | yes | — | SMTP login; also used to build the host name |
| `MAILEXAM_PASSWORD` | yes | — | SMTP password |
| `MAILEXAM_PORT` | no | `587` | SMTP port (`587`, `2525`, or `25`) |
| `MAIL_FROM` | no | `noreply@example.test` | Sender address (any test address is fine) |
| `HTTP_HOST` | no | `127.0.0.1` | HTTP bind address (Docker) |
| `HTTP_PORT` | no | `8000` | HTTP listen port |
| `ALLOWED_HOSTS` | no | `127.0.0.1,localhost` | Comma-separated hosts for Django |

For port **587** and **2525**, `EMAIL_USE_TLS` is `True`. For port **25**, it is `False`.

## Project layout

```
.
├── requirements.txt
├── config/settings.py          # Mailexam SMTP settings
├── mailapp/views.py            # POST /mail/test
├── manage.py
├── .env.example
├── Dockerfile                  # for local debugging only
└── docker-compose.yml
```

## Docker (debugging)

Docker is provided for local debugging. For day-to-day development, run the app on the host (see above).

```bash
cp .env.example .env
# edit .env with your credentials

docker compose up --build
```

Then call the same endpoint on the mapped port:

```bash
curl -X POST http://127.0.0.1:8000/mail/test \
  -H 'Content-Type: application/json' \
  -d '{"to":"user@example.test","subject":"Test","body":"Hello"}'
```

Inside the container the server binds to `0.0.0.0:8000`.

## CI

Set these secrets in your CI environment:

```yaml
variables:
  MAILEXAM_LOGIN: $MAILEXAM_LOGIN
  MAILEXAM_PASSWORD: $MAILEXAM_PASSWORD
  MAILEXAM_PORT: "587"
  MAIL_FROM: "noreply@example.test"
```

After sending a message in a test, verify delivery via the [Mailexam API](https://mailexam.ru/api).

For unit tests without network use `EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"`.

## Troubleshooting

**TLS or connection error**

- `EMAIL_HOST` must be `{login}.mailexam.ru`, matching `EMAIL_HOST_USER` / `MAILEXAM_LOGIN`.
- Login and password must come from the same Mailexam project.

**Port 587**

- Enable `EMAIL_USE_TLS = True`.

**Settings not applied**

- Restart `runserver` after changing `.env` or `settings.py`.

**Message not in the dashboard**

- Open the inbox of the same Mailexam project.
- Ensure `EMAIL_BACKEND` is not overridden to console or file backend.

## See also

- [Mailexam Django guide (wiki)](https://wiki.mailexam.ru/en/examples/django/)
- [Flask reference implementation](https://github.com/mailexam/Flask) — another Python stack
- [Sending email in Django](https://docs.djangoproject.com/en/stable/topics/email/)
- [Mailexam API documentation](https://mailexam.ru/api)

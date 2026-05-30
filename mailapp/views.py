import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def mail_test(request):
    data = json.loads(request.body or "{}")

    send_mail(
        subject=data.get("subject", "Django + Mailexam"),
        message=data.get("body", data.get("text", "Mailexam test from Django")),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[data.get("to", "user@example.test")],
    )

    return JsonResponse({"status": "ok"})

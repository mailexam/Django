from django.urls import path

from . import views

urlpatterns = [
    path("mail/test", views.mail_test, name="mail_test"),
]

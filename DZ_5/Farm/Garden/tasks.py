from django.core.mail import send_mail
from Farm.celery import app
from Garden.models import Contact


@app.tasks
def send_spam_email(user_email):
    def send(user_email):
        send_mail(
            'Example letter',
            [user_email],
            fail_silently=False,
        )
    send(user_email)


@app.tasks
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Example letter what send every 10 minute',
            [contact.mail],
            fail_silently=False,
        )

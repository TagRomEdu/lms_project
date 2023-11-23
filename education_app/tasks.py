from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_update_message(title, subscriber_list, email):

    send_mail(
        subject="Course is updated!",
        message=f'The course "{title}" has been updated.',
        from_email=email,
        recipient_list=subscriber_list
    )

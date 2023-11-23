from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users_app.models import User


@shared_task
def check_user_activity():
    deadline = timezone.now() - timedelta(days=30)
    user_list = User.objects.all()

    for user in user_list:
        if user.last_login and user.last_login < deadline:  # На тот случай, если пользователь не входил ни разу и last_login is None.
            user.is_active = False
            user.save()

from django.core.management import BaseCommand

from education_app.models import Course
from payment_app.models import Payment
from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment = Payment.objects.create(
            user=User.objects.all()[0],
            paid_course=Course.objects.get(pk=2),
            amount=100,
            method='cash'
        )
        payment.save()

from django.core.management import BaseCommand

from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='m@sster.ru',
            first_name='Roman',
            last_name='Tagirov'
        )
        user.save()

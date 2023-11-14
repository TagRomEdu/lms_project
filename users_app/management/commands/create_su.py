from django.core.management import BaseCommand

from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='m@sster.ru',
            first_name='Roman',
            last_name='Tagirov',
            is_superuser=True,
            is_staff=True
        )
        user.set_password('Aa12345!')
        user.save()

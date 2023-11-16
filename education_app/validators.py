import re

from rest_framework.serializers import ValidationError


class DescriptionValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pattern = re.compile(r'http[s]?://[^\s]+')
        description = dict(value).get(self.field)
        links = re.findall(pattern, description)
        if not all('youtube.com' in link for link in links):
            raise ValidationError('У вас тут запрещёночка в описании! Можно ссылки на ютаб, другое под санкциями.')


from django.db import models
from django.utils.translation import gettext_lazy as _

from users_app.models import NULLABLE


class Course(models.Model):
    title = models.CharField(_("title"), max_length=150)
    preview = models.ImageField(_("preview"), upload_to='preview/', **NULLABLE)
    description = models.TextField(_("description"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(_("title"), max_length=250)
    description = models.TextField(_("description"))
    preview = models.ImageField(_("preview"), upload_to='lesson_preview/', **NULLABLE)
    url = models.URLField(_("link to video"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
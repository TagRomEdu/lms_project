from django.db import models
from django.utils.translation import gettext_lazy as _

from education_app.models import Course, Lesson
from users_app.models import User, NULLABLE


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(_("payment date"), auto_now_add=True)
    paid_course = models.ForeignKey(on_delete=models.CASCADE, to=Course, **NULLABLE, related_name='paid_course')
    paid_lesson = models.ForeignKey(on_delete=models.CASCADE, to=Lesson, **NULLABLE, related_name='paid_lesson')
    amount = models.PositiveIntegerField(_("payment amount"))
    method = models.CharField(_("payment method"), choices=[('cash', 'Наличные'), ('transfer', 'Перевод денег')],
                              max_length=20)
    stripe_id = models.CharField(_("link to payment"), **NULLABLE)

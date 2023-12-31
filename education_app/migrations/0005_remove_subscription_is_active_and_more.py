# Generated by Django 4.2.7 on 2023-11-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_app', '0004_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='is_active',
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('user', 'course'), name='unique_subscription'),
        ),
    ]

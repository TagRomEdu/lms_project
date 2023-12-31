# Generated by Django 4.2.7 on 2023-11-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview/', verbose_name='preview')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson_preview/', verbose_name='preview')),
                ('url', models.URLField(verbose_name='link to video')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]

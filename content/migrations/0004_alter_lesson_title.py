# Generated by Django 5.0.2 on 2024-02-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_lesson_delete_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='название'),
        ),
    ]

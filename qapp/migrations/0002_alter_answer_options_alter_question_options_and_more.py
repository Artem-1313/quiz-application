# Generated by Django 4.0 on 2021-12-10 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'Відповіді'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'Питання'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Тест'},
        ),
    ]

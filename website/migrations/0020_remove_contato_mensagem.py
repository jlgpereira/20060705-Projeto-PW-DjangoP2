# Generated by Django 3.2.4 on 2021-06-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_contato_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='mensagem',
        ),
    ]

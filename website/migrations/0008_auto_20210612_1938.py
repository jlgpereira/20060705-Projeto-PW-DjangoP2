# Generated by Django 3.2.4 on 2021-06-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210612_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='opiniao',
            name='p6',
            field=models.CharField(choices=[('Definitivamente sim', 'Definitivamente sim'), ('Provavelmente sim', 'Provavelmente sim'), ('Não sei', 'Não sei'), ('Provavelmente não', 'Provavelmente não'), ('Definitivamente não', 'Definitivamente não')], default=True, max_length=19),
        ),
        migrations.AddField(
            model_name='opiniao',
            name='p7',
            field=models.TextField(max_length=4000, null=True),
        ),
    ]

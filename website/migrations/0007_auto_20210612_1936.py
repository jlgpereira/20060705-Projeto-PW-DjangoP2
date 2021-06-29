# Generated by Django 3.2.4 on 2021-06-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_opiniao_p2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opiniao',
            name='p2',
        ),
        migrations.AddField(
            model_name='opiniao',
            name='p3',
            field=models.CharField(choices=[('Sim, tudo', 'Sim, tudo'), ('Sim, uma parte', 'Sim, uma parte'), ('Não, nada', 'Não, nada')], default=True, max_length=15),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-12 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_opiniao_p5'),
    ]

    operations = [
        migrations.AddField(
            model_name='opiniao',
            name='p2',
            field=models.CharField(blank=True, choices=[('Pesquisa na web', 'Pesquisa na web'), ('Recomendado por um amigo(a)/familiar/colega', 'Recomendado por um amigo(a)/familiar/colega'), ('Outro', 'Outro')], max_length=255, null=True),
        ),
    ]

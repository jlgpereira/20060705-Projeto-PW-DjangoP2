# Generated by Django 3.2.4 on 2021-06-14 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20210613_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('designacao', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('duracao', models.IntegerField()),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salas', to='website.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('apelido', models.CharField(max_length=64)),
                ('aula', models.ManyToManyField(blank=True, related_name='aulas', to='website.Aula')),
            ],
        ),
    ]

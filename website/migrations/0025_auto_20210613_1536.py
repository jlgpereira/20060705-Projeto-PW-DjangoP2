# Generated by Django 3.2.4 on 2021-06-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_quiz_p10'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='p2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='p7',
            field=models.DateField(),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest',
            name='user',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]

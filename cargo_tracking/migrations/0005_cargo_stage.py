# Generated by Django 4.1.7 on 2023-05-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_tracking', '0004_cargo_reciever_city_cargo_sender_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='stage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

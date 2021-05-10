# Generated by Django 3.2.2 on 2021-05-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscription_type',
            field=models.IntegerField(choices=[(0, 'Free'), (1, 'Plus'), (2, 'Pro')], default=0),
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_alter_subscription_subscription_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email_address',
            field=models.EmailField(max_length=320),
        ),
    ]

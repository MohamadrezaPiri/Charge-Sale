# Generated by Django 4.2 on 2023-04-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0008_alter_creditorder_status_alter_saleorder_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='credit',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

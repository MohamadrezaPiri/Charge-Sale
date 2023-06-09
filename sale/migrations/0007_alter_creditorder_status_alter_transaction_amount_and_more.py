# Generated by Django 4.2 on 2023-04-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_creditorder_status_transaction_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditorder',
            name='status',
            field=models.CharField(choices=[('COM', 'Completed'), ('FAI', 'Failed')], default='COM', max_length=3),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('COM', 'Completed'), ('FAI', 'Failed')], default='COM', max_length=3),
        ),
    ]

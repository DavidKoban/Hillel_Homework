# Generated by Django 3.1.7 on 2022-08-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.IntegerField(default=0)),
                ('order_number', models.IntegerField(default=0, unique=True)),
                ('cost_usd', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cost_uah', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_time', models.DateField()),
            ],
        ),
    ]
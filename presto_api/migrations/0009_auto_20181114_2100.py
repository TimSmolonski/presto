# Generated by Django 2.1.2 on 2018-11-14 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presto_api', '0008_auto_20181114_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='sub_toppings',
        ),
        migrations.AddField(
            model_name='topping',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='sub_toppings', to='presto_api.Topping'),
        ),
    ]
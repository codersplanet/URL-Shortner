# Generated by Django 2.2.2 on 2019-08-01 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlmgmt', '0003_auto_20190801_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(max_length=50, primary_key=True, serialize=False),
        ),
    ]

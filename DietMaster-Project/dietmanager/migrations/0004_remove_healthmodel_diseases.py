# Generated by Django 3.0.3 on 2020-02-29 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietmanager', '0003_auto_20200229_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthmodel',
            name='diseases',
        ),
    ]

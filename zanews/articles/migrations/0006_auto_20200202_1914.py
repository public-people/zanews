# Generated by Django 2.2.9 on 2020-02-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200202_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body_text',
            field=models.TextField(blank=True),
        ),
    ]

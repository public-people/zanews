# Generated by Django 2.2.9 on 2020-02-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200131_0715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_name',
        ),
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=300),
        ),
    ]

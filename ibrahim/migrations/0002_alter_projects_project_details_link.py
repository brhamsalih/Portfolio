# Generated by Django 4.2.4 on 2023-08-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibrahim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_details_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]

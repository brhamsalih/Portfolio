# Generated by Django 4.2.4 on 2023-08-19 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibrahim', '0006_remove_projects_main_project_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='publication_date',
            field=models.DateField(null=True),
        ),
    ]

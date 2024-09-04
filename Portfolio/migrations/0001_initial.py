# Generated by Django 4.2.15 on 2024-09-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('photo', models.ImageField(upload_to='project_photos/')),
            ],
        ),
    ]

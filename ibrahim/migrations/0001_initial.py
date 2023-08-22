# Generated by Django 4.2.4 on 2023-08-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_logo', models.CharField(max_length=50)),
                ('welcome', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.CharField(max_length=100)),
                ('btn_name', models.CharField(max_length=50)),
                ('main_title_contact', models.CharField(max_length=50)),
                ('contact_phone', models.IntegerField()),
                ('contact_email', models.EmailField(max_length=200)),
                ('copyright', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title_project', models.CharField(max_length=50)),
                ('main_project_title', models.CharField(max_length=20)),
                ('project_title', models.CharField(max_length=20)),
                ('project_description', models.CharField(max_length=100)),
                ('projec_img', models.ImageField(upload_to='ProjectImg/%y/%m/%d')),
                ('project_details_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title_service', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=20)),
                ('service_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_social_media', models.CharField(max_length=50, verbose_name='Name')),
                ('social_link', models.URLField()),
            ],
            options={
                'verbose_name': 'Social Media Links',
            },
        ),
    ]

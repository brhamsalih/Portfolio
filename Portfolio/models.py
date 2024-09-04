from django.db import models

# Create your models here

class Personal(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='personal_photos/')
    uploaded_file = models.FileField(upload_to='uploaded_files/')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=200)
    photo = models.ImageField(upload_to='project_photos/')

    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=255)
   
    def __str__(self):
        return self.name

class SocialLinks(models.Model):
    social_name = models.CharField(max_length=255)
    social_icone = models.CharField(max_length=255)
    social_links = models.URLField(max_length=200)

    def __str__(self):
        return self.social_name

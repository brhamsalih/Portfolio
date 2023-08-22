from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name_logo = models.CharField(max_length=50)
    main_logo = models.CharField(max_length=200, blank=True)
    welcome = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=100)
    btn_name = models.CharField(max_length=50)
    main_title_service = models.CharField(max_length=20, default="services")
    main_project_title = models.CharField(max_length=20, default="projects")
    main_title_contact = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=14)
    contact_email=models.EmailField(max_length=200)
    copyright = models.CharField(max_length=50)

    def __str__(self):
        return self.name_logo
    
    
class SocialLinks(models.Model):
    name_social_media = models.CharField(max_length=50, verbose_name='Name')
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name_social_media
    
    class Meta:
        verbose_name = "Social Media Links"

class Services(models.Model):
    icon = models.CharField(max_length=200, blank=True)
    service_title = models.CharField(max_length=20)
    service_description = models.CharField(max_length=200) 

    def __str__(self):
        return self.service_title

class Projects(models.Model):
    project_title = models.CharField(max_length=20)
    project_description = models.CharField(max_length=100)
    project_img = models.ImageField(upload_to='ProjectImg/%y/%m/%d')
    project_details_link = models.URLField(max_length=200,default="localhost", blank=True, null=True)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return self.project_title
    
    class Meta:
        pass
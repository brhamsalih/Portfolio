from django.contrib import admin

# Register your models here.
from .models import Project, Skills, Personal, SocialLinks
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Personal)
admin.site.register(SocialLinks)
from django.http import HttpResponse
from django.template import loader

from . models import *

def view_items(request):
    template = loader.get_template('ibrahim/main.html')
    queryset = {
        "portfolio" : Portfolio.objects.all(),
        "link" : SocialLinks.objects.all(),
        "services" : Services.objects.all(),
        "projects" : Projects.objects.all().order_by('-id'),
    }
    '''context = {
        'portfolio':queryset.get("portfolio"),
        'link':queryset.get("link"),
        'services':queryset.get("services"),
        'projects':queryset.get("projects"),
    }'''
    return HttpResponse(template.render(queryset, request))

'''

def view_items(request):
    context = {
        "portfolio" : Portfolio.objects.all(),
        "link" : SocialLinks.objects.all(),
        "services" : Services.objects.all(),
        "projects" : Projects.objects.all(),
    }

       return render(request, 'ibrahim/main.html', context)


'''
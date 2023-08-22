from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_items, name='Home'),
   # path('', views.SocialLink.as_view(), name='Home')
]



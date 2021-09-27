from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('servicios', views.servicios, name='servicios'),
    path('contacto', views.contacto, name='contacto'),
    path('conoceme', views.conoceme, name='conoceme'),
    path('opiniones', views.opiniones, name='opiniones'),
]

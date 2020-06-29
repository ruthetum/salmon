from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('streaming/', views.streamingPage, name="streamingPage"),
    path('credit/', views.creditPage, name="creditPage"),
    path('preparing/', views.preparePage, name="preparePage"),
    path('cornell/', views.cornellPage, name="cornellPage"),
]
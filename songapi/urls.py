from django.urls import path, include
from rest_framework import routers
from songapi import views

routers = routers.DefaultRouter()
routers.register(r'songs', views.SongViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
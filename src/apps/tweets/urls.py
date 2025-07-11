from django.urls import path

from apps.tweets import views

urlpatterns = [
    path('', views.home, name='home'),
]

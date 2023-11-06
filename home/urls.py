from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),

]

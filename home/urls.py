from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.reg,name='register'),
    path('login', views.log,name='login'),
    path('logout', views.logout, name='logout'),

]

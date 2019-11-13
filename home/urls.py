from django.urls import path
from . import views

urlpatterns = [
    path('', views.log),
    path('register', views.reg,name='register'),
    path('login', views.log,name='login'),
    path('logout', views.logout, name='logout'),

]

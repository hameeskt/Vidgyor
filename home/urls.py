from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.reg,name='register'),
    path('login', views.log,name='login'),
    path('logout', views.logout, name='logout'),
    path('video_upload', views.video_upload, name='video_upload'),
    path('add_category', views.add_category, name='category_upload'),
    path('add_tag', views.add_tag, name='tag_upload'),
    # path('success', views.success, name='success'),
    path('details/<int:id>/', views.details, name='details'),
    # path('search', views.search, name='search'),

]

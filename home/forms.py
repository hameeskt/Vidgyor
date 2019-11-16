from django import forms
from .models import *

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file','desc','type','tag','thumb','status','duration','category','uploaded_by']


class VideoEditForm(VideoForm):
    class Meta:
        model = Video
        fields = ['title','desc','tag' ,'type', 'category']


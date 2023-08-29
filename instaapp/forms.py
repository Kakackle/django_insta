from django import forms

from django.contrib.auth.models import User
from .models import Post, Tag, Comment

class PostForm(forms.ModelForm):
    new_tag_1 = forms.CharField(max_length=40, help_text="add a new tag (optional)", required=False)
    new_tag_2 = forms.CharField(max_length=40, help_text="add a new tag (optional)", required=False)
    new_tag_3 = forms.CharField(max_length=40, help_text="add a new tag (optional)", required=False)
    description = forms.CharField(max_length=1000, widget=forms.Textarea())
    
    class Meta:
        model = Post
        fields = ('description', 'post_image', 'tags')
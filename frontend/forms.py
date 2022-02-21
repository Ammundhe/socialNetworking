from django import forms
from post.models import Post, MediaFiles

class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title']

class mediaForm(forms.ModelForm):
    class Meta:
        model=MediaFiles
        fields=['images', 'videos']
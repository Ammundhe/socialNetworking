from dataclasses import fields
from pyexpat import model
from django import forms
from post.models import Post, MediaFiles, Post_comment

class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title']

class mediaForm(forms.ModelForm):
    class Meta:
        model=MediaFiles
        fields=['images', 'videos']

class PostCommentform(forms.ModelForm):
    class Meta:
        model=Post_comment
        fields=['comment']
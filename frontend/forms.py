from django import forms
from post.models import Post, MediaFiles, Post_comment
from page.models import Page, PagePost, PageMedia


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

class Mypageform(forms.ModelForm):
    class Meta:
        model=Page
        fields=['name',]

class PagePostForm(forms.ModelForm):
    class Meta:
        model=PagePost
        fields=['title']

class PageMediaForm(forms.ModelForm):
    class Meta:
        model=PageMedia
        fields=['Pageimges','Page_videos']
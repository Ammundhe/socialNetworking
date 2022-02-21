from django.shortcuts import  redirect, render
from django.views import View
from friends.models import Myuser
from post.models import Post, MediaFiles
from .forms import mediaForm, Postform
from datetime import date


class HomePage(View):
    template_name='home-page.html'
    postform=Postform
    mediaform=mediaForm

    def get(self, request):
        friends=Myuser.objects.values().filter(user=request.user)
        textform=self.postform()
        Mediaform=self.mediaform
        friends_id=[]
        for friend in friends:
            friends_id.append(friend['friends_id'])
            friends_id.append(friend['user_id'])
        posts=Post.objects.filter(user_id__in=friends_id).order_by("-id")
        context={
            'posts':posts,
            'textform':textform,
            'Mediaform':Mediaform,
            
        }
        return render(request, self.template_name, context)

    def post(self, request):
        try:

            if request.POST.get('title'):
                title=request.POST.get('title')
                images=request.POST.get('images')
                videos=request.POST.get('videos')
                post=Post.objects.create(
                    user=request.user,
                    title=title,
                    date=date.today()
                )
                MediaFiles.objects.create(
                    post=post,
                    images=images,
                    videos=videos,
                )
                return redirect("HomePage")
            if request.POST.get("like"):
                post_id=request.POST.get("like")
                post=Post.objects.get(id=post_id)
                post.like=int(post.like)+1
                post.save()
                return redirect("HomePage")

            if request.POST.get("dislike"):
                post_id=request.POST.get("dislike")
                post=Post.objects.get(id=post_id)
                post.dislike=int(post.dislike)+1
                post.save()
                return redirect("HomePage")
            if request.POST.get("text"):
                print(request.POST.get("text"))
                return redirect("HomePage")
        except:
            friends=Myuser.objects.values().filter(user=request.user)
            textform=self.postform()
            Mediaform=self.mediaform
            friends_id=[]
            for friend in friends:
                friends_id.append(friend['friends_id'])
                friends_id.append(friend['user_id'])
            posts=Post.objects.filter(user_id__in=friends_id)
            context={
                'posts':posts,
                'textform':textform,
                'Mediaform':Mediaform,
                
            }
            return render(request, self.template_name, context)
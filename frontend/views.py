from django.shortcuts import  redirect, render
from django.views import View
from friends.models import Myuser
from post.models import Post, MediaFiles, Post_comment
from .forms import mediaForm, Postform, PostCommentform, Mypageform, PagePostForm,PageMediaForm
from datetime import date
from django.contrib.auth.models import User
from page.models import Page, PageLikes, PageMedia, PagePost

class HomePage(View):
    template_name='home-page.html'
    postform=Postform
    mediaform=mediaForm
    commentform=PostCommentform
    pageform=Mypageform

    def get(self, request):
        friends=Myuser.objects.values().filter(user=request.user)
        pages=Page.objects.filter(user=request.user)
        textform=self.postform()
        Mediaform=self.mediaform()
        postcommentform=self.commentform()
        MypageForm=self.pageform()
        friends_id=[]
        for friend in friends:
            friends_id.append(friend['friends_id'])
            friends_id.append(friend['user_id'])
        posts=Post.objects.filter(user_id__in=friends_id).order_by("-id")
        context={
            'posts':posts,
            'textform':textform,
            'Mediaform':Mediaform,
            'postcommentform':postcommentform,
            'MypageForm':MypageForm,
            'pages':pages,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        try:

            if request.POST.get('title'):
                title=request.POST.get('title')
                images=request.FILES.get('images')
                videos=request.FILES.get('videos')
                media=Post.objects.create(
                    user=request.user,
                    title=title,
                    date=date.today()
                )
                file=MediaFiles.objects.create(
                    post=media,
                    images=images,
                    videos=videos
                )
                file.save()
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
            if request.POST.get("comment"):
                comment=request.POST.get("comment")
                id=request.POST.get("post_id")
                Post_comment.objects.create(
                    post_id=id,
                    comment=comment,
                    user=request.user
                )
                return redirect("HomePage")
            if request.POST.get("name"):
                name=request.POST.get("name")
                Page.objects.create(
                    user=request.user,
                    name=name
                )
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


class Friendlist(View):
    template_name='friends-list.html'

    def get(self, request):
        if request.GET.get("search"):
            search=request.GET.get("search")       
            friends=User.objects.filter(username__icontains=search)
            myfriends=Myuser.objects.filter(user=request.user)
            context={
                'friends':friends,
                'myfriends':myfriends,
            }
            return render(request, self.template_name, context)
        friends=User.objects.all()
        myfriends=Myuser.objects.filter(user=request.user)
        context={
            'friends':friends,
            'myfriends':myfriends,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.POST.get('submit'):
            friends_id=request.POST.get('submit')
            Myuser.objects.create(
                user=request.user,
                friends_id=friends_id
            )
        elif request.POST.get('unfriend'):
            friend_id=request.POST.get('unfriend')
            friend=Myuser.objects.get(id=friend_id).delete() 
        return redirect("Friendslist")

class MyPage(View):
    template_name="my-page.html"
    page_form_class=PagePostForm
    page_media_class=PageMediaForm

    def get(self, request, page_id):
        page=Page.objects.get(id=page_id)
        friends=User.objects.all()
        pageLike=PageLikes.objects.filter(page_id=page_id)
        pagePost=PagePost.objects.filter(page_id=page_id)
        page_form=self.page_form_class()
        media_form=self.page_media_class()
        context={
            'page':page,
            'friends':friends,
            'pagePost':pagePost,
            'pageLike':pageLike,
            'page_form':page_form,
            'media_form':media_form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, page_id):
        if request.POST.get('title'):
            title=request.POST.get('title')
            Pageimges=request.FILES.get('Pageimges')
            Page_videos=request.FILES.get('Page_videos')
            Page_post=PagePost.objects.create(
                user=request.user,
                page_id=page_id,
                title=title,
                date=date.today()
            )
            media=PageMedia.objects.create(
                page_id=page_id,
                Page_post=Page_post,
                Pageimges=Pageimges,
                Page_videos=Page_videos
            )
            media.save()
            return redirect("MyPage" ,page_id=page_id)
     
            
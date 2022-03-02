from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="HomePage"),
    path('friends-list', views.Friendlist.as_view(), name="Friendslist"),
    path('mypage/<int:page_id>', views.MyPage.as_view(), name="MyPage"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('login', views.LoginPage.as_view(), name="LoginPage" ),
    path('logout', views.Logout, name="LogoutPage" ),
    path('user-info', views.CreateAccount.as_view(), name="userInfo"),
    path('personal-info', views.PersonalInfo.as_view(), name="PersonalInfo"),
    path('profile-picture', views.profilePicture.as_view(), name="profilePicture"),
    
]

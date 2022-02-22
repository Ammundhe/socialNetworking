from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as authlogin, logout as authlogout, authenticate
from .forms import createAccountform

class LoginPage(View):
    template_name="login.html"
    form_class= AuthenticationForm

    def get(self, request):
        form=self.form_class()
        context={
            'form':form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            authlogin(request, form.get_user())
            return redirect("HomePage")
        return redirect("LoginPage")

def Logout(request):
    authlogout(request)
    return redirect("LoginPage")


class CreateAccount(View):
    template_name="create-account.html"
    form_class=UserCreationForm


    def get(self, request):
        form=self.form_class()
        context={
            'form':form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            authlogin(request, user)
            return redirect("PersonalInfo")
        return redirect("userInfo")


class PersonalInfo(View):
    template_name="personal-info.html"
    form_class= createAccountform

    def get(self, request):
        form=self.form_class()

        context={
            'form':form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
       form=self.form_class(data=request.POST, instance=request.user)
       if form.is_valid():
           form.save()
           return redirect("HomePage")
       return redirect("PersonalInfo")

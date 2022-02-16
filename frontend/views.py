from django.shortcuts import render
from django.views import View


class HomePage(View):
    template_name='home-page.html'

    def get(self, request):
        return render(request, self.template_name)
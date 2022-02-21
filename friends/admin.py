from django.contrib import admin
from friends.models import Myuser

class MyuserAdmin(admin.ModelAdmin):
    list_display=['user', 'friends']

admin.site.register(Myuser, MyuserAdmin)
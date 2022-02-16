from django.contrib import admin, messages
from groups.models import Group, GroupMedia, GroupMember, GroupPost


def hidePost(self, request, queryset):
    queryset.update(status=False)
    messages.success(request, 'selected post marked as a hide')

def unhidePost(self, request, queryset):
    queryset.update(status=True)
    messages.success(request, 'selected post marked as a unhided')


class GroupMediaAdmin(admin.TabularInline):
    model=GroupMedia
    extra=1
    classes=("collapse",)

class GroupPostAdmin(admin.ModelAdmin):
    list_display=('group', 'title', 'status', 'date')
    list_filter=['status',]
    search_fields=['title', 'group']
    actions=[hidePost, unhidePost]
    inlines=[GroupMediaAdmin]

admin.site.register(GroupPost, GroupPostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display=('name', 'status')
    list_filter=('status',)
    search_fields=['name']
    actions=[hidePost, unhidePost]

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember)

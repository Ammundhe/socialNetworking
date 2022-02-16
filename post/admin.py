from django.contrib import admin, messages
from post.models import Post, MediaFiles

def hidePost(self, request, queryset):
    queryset.update(status=False)
    messages.success(request, 'selected post marked as a hide')

def unhidePost(self, request, queryset):
    queryset.update(status=True)
    messages.success(request, 'selected post marked as a unhided')

class mediaFileAdmin(admin.TabularInline):
    model=MediaFiles
    extra=1
    classes=('collapse',)

class PostAdmin(admin.ModelAdmin):
    list_display=['title','date', 'status', 'user']
    list_filter=('status',)
    search_fields=['title', 'user']
    actions=[hidePost, unhidePost]
    inlines=[mediaFileAdmin]

admin.site.register(Post,PostAdmin)
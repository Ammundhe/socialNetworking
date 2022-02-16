from django.contrib import admin, messages
from page.models import Page, PageMedia, PagePost, PageLikes

def hidePost(self, request, queryset):
    queryset.update(status=False)
    messages.success(request, 'selected post marked as a hide')

def unhidePost(self, request, queryset):
    queryset.update(status=True)
    messages.success(request, 'selected post marked as a unhided')


class PageMediaAdmin(admin.TabularInline):
    model=PageMedia
    extra=1
    classes=("collapse",)

class PagePostAdmin(admin.ModelAdmin):
    list_display=('page', 'title', 'status', 'date')
    list_filter=['status',]
    search_fields=['title', 'page']
    actions=[hidePost, unhidePost]
    inlines=[PageMediaAdmin]

admin.site.register(PagePost, PagePostAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display=('name', 'status')
    list_filter=('status',)
    search_fields=['name']
    actions=[hidePost, unhidePost]

admin.site.register(Page, PageAdmin)
admin.site.register(PageLikes)

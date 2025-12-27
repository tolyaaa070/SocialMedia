from django.contrib import admin
from .models import *
class PostContentInline(admin.TabularInline):
    model = PostContent
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostContentInline]
    list_display = ('id', 'author', 'hashtags_list', 'created_date')
    filter_horizontal = ('hashtag', 'people')

    def hashtags_list(self, obj):
        return ", ".join(i.hashtag_name for i in obj.hashtag.all())

    hashtags_list.short_description = 'Hashtags'

admin.site.register(HashTag)
admin.site.register(PostLike)
admin.site.register(Review)
admin.site.register(ReviewLike)
admin.site.register(Notes)
admin.site.register(Chat)
admin.site.register(ArchiveItems)
admin.site.register(Stories)
admin.site.register(Message)
admin.site.register(UserProfile)

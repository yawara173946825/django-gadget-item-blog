from django.contrib import admin
from blog.models import Post, Category, Tag, ContentImage
# Register your models here.


class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


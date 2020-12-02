from django.contrib import admin
from blog.models import Post,Comment,Category
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fields = ['title','category','author']
    search_fields = ['title','category','author']
    list_filter = ['date_created','category']
    list_display = ['title','category', 'author','date_created','comments']

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Post)
# admin.site.register(Post)

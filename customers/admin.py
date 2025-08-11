from django.contrib import admin
from .models import Customer, Blog, Comment
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("cid","cname","address")
    search_fields = ("cid","cname")

admin.site.register(Customer,CustomerAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","desc")
    search_fields = ("title",)

admin.site.register(Blog,BlogAdmin)    

class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog","comment")
    search_fields = ("blog",)

admin.site.register(Comment,CommentAdmin)    
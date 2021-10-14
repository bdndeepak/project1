from django.contrib import admin
from .models import Post
# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ['title','desc']

admin.site.register(Post,AdminPost)
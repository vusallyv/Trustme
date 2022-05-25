from django.contrib import admin

# Register your models here.

from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'author']
    list_filter = ['created_at']
    exclude = ['slug']


admin.site.register(Blog, BlogAdmin)
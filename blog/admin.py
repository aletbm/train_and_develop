from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author")
    readonly_fields = ("created", "updated")


admin.site.register(Post, PostAdmin)

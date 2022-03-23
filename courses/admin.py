from django.contrib import admin
from courses.models import Course, Category
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'display_category')
    readonly_fields = ("created", "updated")


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
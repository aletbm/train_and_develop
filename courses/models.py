from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class Course(models.Model):
    def display_category(self):
        return ', '.join([ cat.category for cat in self.category.all()[:5] ])

    image = models.ImageField(upload_to="courses", null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    display_category.short_description = 'Category'

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

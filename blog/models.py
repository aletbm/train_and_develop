from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=70)
    date = models.DateField()
    text = models.CharField(max_length=400)
    head_post = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title
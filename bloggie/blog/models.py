from django.db import models
from django.contrib.auth import get_user_model

from froala_editor.fields import FroalaField


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = FroalaField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments'),
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField()
    date = models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.comment}'
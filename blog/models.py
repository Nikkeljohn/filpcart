from django.db import models
from django.contrib.auth.models import User
from django import forms
from filpcart import settings



STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2,)
    excerpt = models.TextField(blank=True)
    brand = models.CharField(default=0, max_length=200, unique=True)
    review = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return f'Comment {self.body} by {self.name}'
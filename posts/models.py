from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .base_models import BaseModels


class Post(BaseModels):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    catalog = models.ForeignKey('catalogs.Catalog',on_delete=models.CASCADE,related_name='products')
    author = models.ForeignKey('authors.Author',on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    tag = models.ManyToManyField('tags.Tag',related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('posts:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return self.name


class Comment(BaseModels):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    comment = models.TextField()
    post = models.ForeignKey(
        'Post',  # Use a string reference to avoid direct import
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )

    def __str__(self):
        return self.name
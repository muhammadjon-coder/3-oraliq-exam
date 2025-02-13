from django.db import models
from posts.models import Post
from posts.base_models import BaseModels


class Catalog(BaseModels):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, related_name='catalogs')

    def __str__(self):
        return self.name

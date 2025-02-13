from posts.base_models import BaseModels
from django.db import models


class Author(BaseModels):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    bod = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='authors/')

    def __str__(self):
        return f"{self.full_name}"

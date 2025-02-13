from django.db import models
from posts.base_models import BaseModels


class Tag(BaseModels):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

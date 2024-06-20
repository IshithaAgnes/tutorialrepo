from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
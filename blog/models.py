from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    article = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_edit', kwargs={'pk':self.pk})

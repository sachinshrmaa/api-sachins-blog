from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True )
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='post-thumbnail/')
   

    def __str__(self):
        return self.title
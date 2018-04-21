from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_titel = models.CharField(max_length=200)
    blog_body = models.TextField()
    blog_author = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')

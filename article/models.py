from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	publish_date = models.DateTimeField('date published')
	likes = models.IntegerField()

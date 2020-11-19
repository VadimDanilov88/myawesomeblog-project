from django.db import models
from django.db import models

class Post(models.Model):
	event_image=models.ImageField(upload_to="event_images/")
	title=models.CharField(max_length=300)
	data=models.DateTimeField()
	text=models.TextField()
# Create your models here.

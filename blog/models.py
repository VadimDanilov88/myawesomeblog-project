from django.db import models


class Post(models.Model):
	event_image=models.ImageField(upload_to="event_images/")
	title=models.CharField(max_length=300)
	data=models.DateTimeField()
	text=models.TextField()


def get_summary(self):
    	return self.text[:70]

from django.db import models

# Create your models here.
class files (models.Model):
	file = models.FileField(upload_to='myFiles/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
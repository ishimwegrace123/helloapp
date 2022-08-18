from django.db import models

# Create your models here.
class UploadMovie(models.Model):
    image = models.ImageField(upload_to="img/%y")
    title = models.CharField(max_length=100)
    main_actors = models.TextField()
    genre = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    def __str__(self):
        return self.title       
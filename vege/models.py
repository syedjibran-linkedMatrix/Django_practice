from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', default='default_image.jpg')

    def __str__(self):
        return self.name

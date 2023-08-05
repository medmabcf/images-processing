
from django.db import models
from image_cropping import ImageCropField, ImageRatioField

class MyModel(models.Model):
    image = ImageCropField(upload_to='images/')
    cropping = ImageRatioField('image', '430x360')

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
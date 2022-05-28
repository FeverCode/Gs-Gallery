from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.location_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def __str__(self):
        return self.category_name
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=100)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    

@classmethod
def get_image_by_id(cls,id):
    image = cls.objects.filter(id=id)
    return image


@classmethod
def search_image(cls, search_image):
    image = cls.objects.filter(title__icontains=search_image)
    return image


@classmethod
def filter_by_location(cls, location):
    imageLocation = cls.objects.filter(location=location)
    return imageLocation

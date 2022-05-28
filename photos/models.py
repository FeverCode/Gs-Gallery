from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name
    

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
    
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.image_name


@classmethod
def get_image_by_id(cls,id):
    image = cls.objects.filter(id=id)
    return image


@classmethod
def search_image(cls,query):
    image = cls.objects.filter(image_category__name__icontains=query)
    return image


@classmethod
def filter_by_location(cls,query):
    imageLocation = cls.objects.filter(image_location__name__icontains=query)
    return imageLocation

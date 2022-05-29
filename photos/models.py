from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    l_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.l_name

    def save_location(self):
        self.save()
        
    @classmethod
    def get_location(cls):
        location = Location.objects.all()
        return location
    
    @classmethod
    def update_location(cls,id, value):
        cls.objects.filter(id=id).update(image=value)
        
    def delete_location(self):
        self.delete()
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
class Image(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    
    @classmethod
    def search_image(cls, search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image
    
    @classmethod
    def filter_by_location(cls, query):
        imageLocation = cls.objects.filter(location__name__icontains=query)
        return imageLocation
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    @classmethod
    def update_image(cls, id, value):
        image = cls.objects.filter(id=id).update(image=value).all()
        return image
    
    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location
    
    @classmethod
    def view_category(cls,cat):
        category = cls.objects.filter(category=cat)
        return category

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    








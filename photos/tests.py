from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.new_location = Location(name = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
        
class CategoryTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.new_category = Category(category_name = 'Travel')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    # Testing Save Method
    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
        
class ImageTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.new_category = Category(category_name='Travel')
        self.new_category.save()
        
        self.new_location = Location(name='Nairobi')
        self.new_location.save()

        self.new_image = Image(image_name='Nairobi', image_location=self.new_location, image_category=self.new_category, image_description='Beautiful')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # Testing Save Method
    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

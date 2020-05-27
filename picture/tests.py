from django.test import TestCase
from .models import PhotoImage,Category,Location
# Create your tests here.

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        #creating a new location and saving it
        self.new_location=Location(location_name="Mozambique")
        self.new_location.save_location()

    def tearDown(self):
            Location.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.new_location.save_location()
        location =Location.objects.all()
        self.assertTrue(len(location) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.new_location.delete_location()
        location =Location.objects.all()
        self.assertTrue(len(location) == 0)

          # Testing update Method    
    def test_update_location_method(self):
        self.new_location.update_location(name="Mozambique",field="location_name", value="TestMozambique")
        photo =Location.objects.all()
        self.assertTrue(len(photo) ==1)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        #creating a new category and saving it
        self.new_category=Category(title="test")
        self.new_category.save_category()

    def tearDown(self):
            Category.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    # Testing Save Method
    def test_save_method(self):
        self.new_category.save_category()
        category =Category.objects.all()
        self.assertTrue(len(category) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.new_category.delete_category()
        category =Category.objects.all()
        self.assertTrue(len(category) == 0)

          # Testing update Method    
    def test_update_location_method(self):
        self.new_category.update_category(name="test",field="title", value="TestCategory")
        category =Category.objects.all()
        self.assertTrue(len(category) ==1)
    

class PhotoImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        #creating a new location and saving it
        self.new_location=Location(location_name="Mozambique")
        self.new_location.save_location()
        
        #creating a new category and saving it
        self.new_category=Category(title="test")
        self.new_category.save_category()

        #creating a new photo and saving it
        self.photo= PhotoImage(name = 'test1',description="MozambiqueTest",category=self.new_category)
        self.photo.save_photo()

        self.photo.location.add(self.new_location)

    def tearDown(self):
            Category.objects.all().delete()
            Location.objects.all().delete()
            PhotoImage.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,PhotoImage))
        

    # Testing Save Method
    def test_save_method(self):
        self.photo.save_photo()
        photo =PhotoImage.objects.all()
        self.assertTrue(len(photo) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.photo.delete_photo()
        photo =PhotoImage.objects.all()
        self.assertTrue(len(photo) == 0)

         # Testing update Method    
    def test_update_category_method(self):
        self.photo.update_photo(name="test1",field="description", value="TestMozambique")
        photo =PhotoImage.objects.all()
        self.assertTrue(len(photo) ==1)

          # Testing search by category Method    
    def test_search_by_category_method(self):
        self.photo.search_by_category(category="test")
        photo =PhotoImage.objects.all()
        self.assertTrue(len(photo) ==1)
    
         # Testing search by id Method    
    def test_get_image_by_id_method(self):
        self.photo.get_image_by_id(id=1)
        photo =PhotoImage.objects.all()
        self.assertTrue(len(photo) ==1)
    
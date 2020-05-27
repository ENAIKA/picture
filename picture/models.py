from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =60)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def update_location(self,name,field,value):
        obj = Location.objects.get(location_name=name)
        obj.field = value
        obj.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    title = models.CharField(max_length =60)

    def save_category(self):
        self.save()

    def update_category(self,name,field,value):
        obj = Category.objects.get(title=name)
        obj.field = value
        obj.save()

    def delete_category(self):
        self.delete()

    

class PhotoImage(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'photos/')
    description= models.TextField( blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(Location)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_photo(self):
        self.save()

    def update_photo(self,name,field,value):
        obj = PhotoImage.objects.get(name=name)
        obj.field = value
        obj.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def search_by_category(cls,category):
        photos = PhotoImage.objects.filter(category__title__icontains=category)
        return photos

    @classmethod
    def filter_by_location(cls,location):
        photos = cls.objects.filter(location__icontains=location)
        return photos
    
    @classmethod
    def get_image_by_id(cls,id):
        photos = cls.objects.filter(id=id)
        return photos

    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos
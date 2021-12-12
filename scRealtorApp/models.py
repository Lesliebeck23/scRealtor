from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Listing(models.Model):
    address = models.CharField(max_length=255)
    added_by = ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True),
    sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.TextField()
    home_photo = models.ImageField(null = True, blank=True, upload_to="images/")
    price = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        #args tells it what specific post to go to
        #return reverse('article-detail', args=(str(self.id)) )
        #This just redirects you to the home page instead of article-details
        return reverse('features')


class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    client_testimonial = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)




from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner_images/')
    
    
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desciption = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    quantity = models.IntegerField(default=1)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    age = models.IntegerField()

    
    def __str__(self):
        return self.name
    
    
    
    
    
    

    
    
    


    
    
    
    






from django.db import models
from django.contrib.auth.models import User

# Create your models here.

   

class Product(models.Model):
    created = models.DateTimeField(auto_now=True , verbose_name="تاريخ الاضافة")
    created_by = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name = "اضيف بواسطة")
    name = models.CharField(max_length=50 , verbose_name="اسم الموديل")
    code = models.CharField(max_length=50 ,null=True , verbose_name="كود الموديل")
    image = models.ImageField(null=True, blank=True , verbose_name="صورة الموديل")
    weight = models.CharField(null=True, blank=True , max_length=15, verbose_name="وزن الموديل" )
    cost = models.CharField(null=True, blank=True , max_length=15 , verbose_name="التكلفة")
    price = models.CharField(null=True, blank=True , max_length=15 , verbose_name="سعر البيع")
    
    def __str__(self):
        return self.name
    
    
    

class Color(models.Model):
    Product = models.ForeignKey(Product, verbose_name ="الموديل", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add =True, verbose_name="تاريخ الاضافة")
    name = models.CharField(max_length=50 , verbose_name="اسم اللون")
    
    def __str__(self):
        return self.name

class Size(models.Model):
    Product = models.ForeignKey(Product, verbose_name ="الموديل", on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now=True, auto_now_add=False , verbose_name="تاريخ الاضافة")
    name = models.CharField(max_length=50 , verbose_name=" المقاس")
    
    def __str__(self):
        return self.name
        
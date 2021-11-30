from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Factory(models.Model):
    created = models.DateTimeField(auto_now_add=True , verbose_name="تاريخ الاضافة")
    created_by = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name = "اضيف بواسطة")
    name = models.CharField(max_length=50 , verbose_name="اسم المصنع")
    image = models.ImageField(null=True, blank=True, verbose_name="صورة المصنع")
    hour_price = models.IntegerField(null=True, blank=True, verbose_name="حساب الساعه" )
    machine_type = models.CharField(null=True, blank=True, max_length=50 , verbose_name="نوع المكنة")
    machine_count = models.IntegerField(null=True , verbose_name="عدد المكن")
    phone = models.CharField(null=True, blank=True, max_length=12 , verbose_name="رقم الموبيل")
    active = models.BooleanField(default=True , verbose_name="يعمل")
    start_date = models.DateField(null=True , verbose_name="تاريخ البداية")
    
    
    def __str__(self):
        return self.name
    
class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True , verbose_name="تاريخ الاضافة")
    price = models.IntegerField(verbose_name="المبلغ")
    factory = models.ForeignKey(Factory , on_delete=models.CASCADE , verbose_name="المصنع")
    recipient = models.CharField(max_length=50 , verbose_name="المستلم")
    admin = models.CharField(max_length=50 , verbose_name="المسئول")
    date = models.DateField(verbose_name="التاريخ")
    
    def __str__(self):
        return self.factory.name
    
       
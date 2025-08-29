from django.db import models
#تمثيل البيانات catogery علئ شكل class 
from django.contrib.auth.models import User
# Create your models here.
#database data
#اطر العمل نمثل الجدول ع شكل كلاس ثم نرحله لداتابيس
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True ,null=True)
    icon =models.CharField(max_length=50 ,blank=True)
    def __str__(self):
        return self.name







class Product(models.Model):
      name = models.CharField(max_length=100)
      price= models.DecimalField(max_digits=10,decimal_places=6)
      color=models.CharField(max_length=100)
      brand=models.CharField(max_length=40)
      image=models.ImageField(upload_to='mobile/images')
      storge = models.CharField(max_length=100)
      #تكامل مرجعي عند حذف البراند ابل مثلا راح ينمسح جميع منتجاتها
      #ربط المنتج اولا مع البراند لان المنتج يحتاج براند واحد
      category = models.ForeignKey(Category, on_delete=models.CASCADE)\
      #في لوحه الاداره احتاج يظهر اسهم
      def __str__(self):
        return self.name
      


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) #connect to user
    session_id=models.CharField(max_length=100 ,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quntity = models.PositiveBigIntegerField(default=0)
    created_at =models.DateField(auto_now_add=True)

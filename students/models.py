from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)  # اسم المدينة
    street = models.CharField(max_length=200)  # اسم الشارع

    def __str__(self):
        return f"{self.city}, {self.street}"  # تمثيل نصي للعنوان

class Student(models.Model):
    name = models.CharField(max_length=100)  # اسم الطالب
    email = models.EmailField(unique=True)  # البريد الإلكتروني
    addresses = models.ManyToManyField('Address')  # علاقة Many-to-Many

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)  # عنوان الصورة
    image = models.ImageField(upload_to='gallery/')  # رفع الصور إلى مجلد gallery/

    def __str__(self):
        return self.title

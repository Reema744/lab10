from django.contrib import admin
from apps.bookmodule.models import Book  # استيراد نموذج Book

admin.site.register(Book)  # تسجيل النموذج في واجهة المسؤول
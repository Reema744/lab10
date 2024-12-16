from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
     path('gallery/upload/', views.upload_image, name='upload_image'),
    path('gallery/', views.gallery_list, name='gallery_list'),
]

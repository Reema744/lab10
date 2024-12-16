from django import forms
from .models import Student, Address ,Gallery


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street']  # حقول العنوان

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'addresses']  # حقول الطالب




class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']  # Fields to be displayed in the form


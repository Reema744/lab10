from django.shortcuts import render ,get_object_or_404, redirect
from .models import Student , Gallery
from .forms import StudentForm
from .forms import GalleryForm


def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('list_students')
    return render(request, 'students/delete.html', {'student': student})

def upload_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')  # Redirect to gallery list
    else:
        form = GalleryForm()
    return render(request, 'students/upload_image.html', {'form': form})

def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'students/gallery_list.html', {'images': images})


from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book  # تأكد من أنك استوردت نموذج Book
from django.db.models import Q
from django.db.models import Count
from .models import Address
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import BookForm


# تعريف قائمة الكتب (لتكون بمثابة بيانات تجريبية)
books_data = [
    {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'},
    {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
]

def index(request):
    return render(request, 'bookmodule/index.html')

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    # البحث عن الكتاب المطلوب باستخدام البيانات التجريبية
    targetBook = next((book for book in books_data if book['id'] == bookId), None)
    
    if targetBook is None:
        raise Http404("Book not found.")
    
    context = {'book': targetBook}  # تمرير الكتاب إلى القالب
    return render(request, 'bookmodule/one_book.html', context)  # تأكد من استخدام القالب الصحيح

def list_books(request):
    # إظهار قائمة الكتب باستخدام البيانات التجريبية
    return render(request, 'bookmodule/list_books.html', {'books': books_data})  # تمرير قائمة الكتب إلى القالب

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def test_header(request):
    return render(request, 'bookmodule/includes/header.html')

def links_page(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search_view(request):
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    # قائمة الكتب
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def book_list_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()  # الحصول على قائمة الكتب
        newBooks = []  # قائمة جديدة لتخزين الكتب المطابقة

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})  # عرض النتائج المطابقة

    # إذا لم يكن هناك طلب POST، قم بعرض جميع الكتب
    books = __getBooksList()
    return render(request, 'bookmodule/bookList.html', {'books': books})

def simple_query(request):
    books = Book.objects.all()  # جلب جميع الكتب كبداية
    
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')

        # بناء الاستعلام بناءً على الخيارات
        if option1 and option2:  # البحث في العنوان والمؤلف
            books = books.filter(title__icontains=keyword) | books.filter(author__icontains=keyword)
        elif option1:  # البحث في العنوان فقط
            books = books.filter(title__icontains=keyword)
        elif option2:  # البحث في المؤلف فقط
            books = books.filter(author__icontains=keyword)

    return render(request, 'bookmodule/bookList.html', {'books': books})


def lookup_query(request):
    # تطبيق الشروط المختلفة على استعلام الكتب
    mybooks = Book.objects.filter(
        author__isnull=False  # اختيار الكتب التي لديها مؤلف
    ).filter(
        title__icontains='and'  # اختيار الكتب التي تحتوي على "and" في العنوان
    ).filter(
        edition__gte=2  # اختيار الكتب ذات الإصدار الثاني أو أعلى
    ).exclude(
        price__lte=100  # استبعاد الكتب التي سعرها 100 أو أقل
    )[:10]  # تحديد أول 10 نتائج فقط

    # التحقق مما إذا كانت هناك نتائج
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task1_view(request):
    books = Book.objects.filter(Q(price__lte=50))
    print(f"Number of books: {books.count()}") 
    return render(request, 'bookmodule/task1.html', {'books': books, 'count': books.count()})

def task2_view(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    print(f"Number of books with edition > 2 and containing 'qu': {books.count()}")
    return render(request, 'bookmodule/task2.html', {'books': books, 'count': books.count()})

def task3_view(request):
    books = Book.objects.filter(
        ~Q(edition__gt=2) & ~(
            Q(title__icontains='qu') | Q(author__icontains='qu')
        )
    )
    print(f"Number of books with edition <= 2 and without 'qu': {books.count()}")
    return render(request, 'bookmodule/task3.html', {'books': books, 'count': books.count()})

def task4_view(request):
    books = Book.objects.order_by('title')
    print(f"Number of books ordered by title: {books.count()}")
    return render(request, 'bookmodule/task4.html', {'books': books, 'count': books.count()})



def task5_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7_view(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    print(f"Cities with student counts: {cities}")
    return render(request, 'bookmodule/task7.html', {'cities': cities})

def list_books(request):
    """عرض قائمة الكتب"""
    books = Book.objects.all()  # جلب جميع الكتب من قاعدة البيانات
    return render(request, 'bookmodule/list_books.html', {'books': books})


def add_book(request):
    """إضافة كتاب جديد"""
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        isbn = request.POST.get('isbn')
        Book.objects.create(title=title, author=author, publication_date=publication_date, isbn=isbn)
        return redirect('list_books')
    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):
    """تعديل بيانات كتاب معين"""
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('publication_date')
        book.isbn = request.POST.get('isbn')
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/edit_book.html', {'book': book})


def delete_book(request, id):
    """حذف كتاب مع تأكيد من المستخدم"""
    book = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        # إذا تم الضغط على زر التأكيد، يتم حذف الكتاب
        book.delete()
        return redirect('list_books')  # إعادة التوجيه إلى قائمة الكتب
    
    # إذا كان الطلب GET، يتم عرض صفحة التأكيد
    return render(request, 'bookmodule/confirm_delete.html', {'book': book})

def add_book_with_form(request):
    """إضافة كتاب باستخدام نموذج Django"""
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books')  # بعد الحفظ، يتم إعادة توجيه المستخدم إلى قائمة الكتب
    return render(request, 'bookmodule/add_book_with_form.html', {'form': form})

def edit_book_with_form(request, id):
    """تعديل كتاب باستخدام نموذج Django"""
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)  # تمرير الكائن الكتاب إلى النموذج
    if form.is_valid():
        form.save()
        return redirect('list_books')  # بعد التعديل، يتم إعادة توجيه المستخدم إلى قائمة الكتب
    return render(request, 'bookmodule/edit_book_with_form.html', {'form': form})
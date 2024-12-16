from django.urls import path
from . import views
from .views import test_header
from .views import book_list_view


urlpatterns = [
    path('search/', book_list_view, name='book_search'),  # تأكد من وجود الشريحة
    path('books/html5/text/formatting/', views.formatting, name='formatting'),
    path('books/html5/listing/', views.listing_view, name='listing'),
    path('books/html5/tables/', views.tables, name='tables_page'),
    path('', views.index, name="books.index"),  # تأكد من أن لديك مسار للجذر
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('test-header/', test_header, name='test_header'),
    path('books/html5/links', views.links_page, name='links_page'),
    path('books/simple/query', views.simple_query, name='book_search'),
    path('books/complex/query', views.lookup_query, name='lookup_query'),
    path('lab8/task1', views.task1_view, name='task1'),
    path('lab8/task2', views.task2_view, name='task2'),
    path('lab8/task3', views.task3_view, name='task3'),
    path('lab8/task4', views.task4_view, name='task4'),
    path('lab8/task5', views.task5_view, name='task5'),
    path('lab8/task7', views.task7_view, name='task7'),
    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),

        # الجزء الثاني: CRUD باستخدام Django Forms
    path('lab9_part2/addbook', views.add_book_with_form, name='add_book_with_form'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_with_form, name='edit_book_with_form'),

]
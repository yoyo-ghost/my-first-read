from django.urls import path
from . import views

app_name = 'read'

#urlを指定して、viewsへ誘導
urlpatterns = [
   path('insert_book', views.Insert_Book, name = 'insert_book'),
   path('books_list', views.books_list, name='books_list'),
   path('update_book/<int:id>', views.update_book, name='update_book')

]

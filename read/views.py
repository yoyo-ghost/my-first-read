from django.shortcuts import render
from . import forms
from .models import Book


# formからのデータを保存、登録画面をhtmlで返す
def Insert_Book(request):
    insert_book = forms.BookForm(request.POST or None)
    if insert_book.is_valid(): #値の形式が正しいなら保存
        insert_book.save()
        insert_book = forms.BookForm()
    return render(
        request, 'form_app/register_page.html', context={
            'insert_book': insert_book 
        }
    )

# 本の一覧
def books_list(request):
    books = Book.objects.all()
    return render(
        request, 'form_app/books_list.html', context={
            'books': books
        }
    )

# 本の編集
def update_book(request, id):
    book = Book.objects.get(id=id)
    update_form = forms.BookUpdateForm(
        initial = {
            'book_title': book.book_title, 'book_author': book.book_author, 'date': book.date, 'text': book.text
        }
    )
    if request.method == 'POST':
        update_form = forms.BookUpdateForm(request.POST or None)
        if update_form.is_valid():
            book.book_title = update_form.cleaned_data['book_title']
            book.book_author = update_form.cleaned_data['book_author']
            book.date = update_form.cleaned_data['date']
            book.text = update_form.cleaned_data['text']
            book.save()

    return render(
        request, 'form_app/update_book.html', context={
            'update_form': update_form,
            'book': book
        }
    )
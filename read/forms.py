#models.pyのBookを取り入れる
from .models import Book
from django import forms

# 読書の登録フォーム
class BookForm(forms.ModelForm):

    book_title = forms.CharField(label='本の名前')
    book_author = forms.CharField(label='著者名')
    date = forms.DateField(label='読んだ日')
    text = forms.CharField(label='感想',widget=forms.Textarea)

    class Meta:
        model = Book #モデルの名前を教える
        fields = '__all__' # フィールドは全て使う


# 読書の編集フォーム
class BookUpdateForm(forms.Form):

    book_title = forms.CharField(label='本の名前')
    book_author = forms.CharField(label='著者名')
    date = forms.DateField(label='読んだ日')
    text = forms.CharField(label='感想',widget=forms.Textarea)
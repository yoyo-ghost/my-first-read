from django.db import models
from django.utils import timezone


# 本の情報 
class Book(models.Model):
    # verbose_nameは管理画面の入力時にbook_titleではなく、タイトルと表示する
    book_title = models.CharField(max_length=50, verbose_name='タイトル')
    book_author = models.CharField(max_length=50, verbose_name='著者')
    date = models.DateField(verbose_name='読んだ日付') 
    text = models.TextField(verbose_name='感想')

    # 下は同じく管理画面でbookの登録時に題名を表示するために必要
    def __str__(self):
        return self.book_title

    # データベースに登録するテーブル名を決める
    class Meta:
        db_table = 'books'

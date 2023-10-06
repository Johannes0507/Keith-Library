from django.db import models


# 書籍類別資料庫
class Genre(models.Model):
    name = models.CharField('書本類型', max_length=200, help_text='輸入你的書籍類別 Ex: 科學、生物、資訊')
    
    def __str__(self):
        return self.name # 回傳書籍類別名稱
    

from django.urls import reverse

# 建構書本資料庫
class Book(models.Model):
    title = models.CharField('書名', max_length=200) # 書本名稱
    author = models.ForeignKey('Author', verbose_name='作者', on_delete=models.SET_NULL, null=True) # 作者
    summary = models.TextField('簡介', max_length=1000, help_text='請輸入書本簡介') # 簡介
    isbn = models.CharField('ISBN編號', max_length=13, help_text='小於13字 <a href="https://www.isbn-international.org/content/what-isbn"> ISBN號碼</a>')
    genre = models.ManyToManyField(Genre, verbose_name='書本類型', help_text='選擇你的書本類別') # 書本類別選項
    language = models.ForeignKey('Language', verbose_name='書本語言', on_delete=models.SET_NULL, null=True, help_text='選擇你的書本語言種類')
    
    # 回傳輸本名稱
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ','.join([genre.name for genre in self.genre.all()[:2]])
    
    display_genre.short_description = '種類'
    
    
import uuid
from django.contrib.auth.models import User # 要加入borrowed的import
from datetime import date

# 建立書本內容資料庫模型
class BookInstance(models.Model):
    id = models.UUIDField('編號', primary_key=True, default=uuid.uuid4, help_text='生成一個在圖書館獨有的書本ID')  # 創建書本ID
    book = models.ForeignKey('Book', verbose_name='書名', on_delete=models.SET_NULL, null=True) # 創建一對多的書本資料 連接到書本的資料庫模型
    imprint = models.CharField('出版商名稱', max_length=200)  # 創建出版商欄位
    due_back = models.DateField('歸還日期', null=True, blank=True) # 設定還書日期
    borrower = models.ForeignKey(User, verbose_name='借書者', on_delete=models.SET_NULL, null=True, blank=True) # 創建一個一對多的借書者欄位
    
    LOAN_STATUS = (
        ('m', '保養中'),
        ('o', '已被租借'),
        ('a', '可租借'),
        ('r', '已預定'),
        )    
    
    status = models.CharField(
        verbose_name='書本狀態',
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='預定中',
        )
     
    
    class Meta:
        ordering = ['due_back'] # 以租借日期排序
        permissions = (("can_mark_returned", "可以看到所有以租借的書本"),)
    
    def __str__(self): 
        return f'{self.id} ({self.book.title})' # 回傳書本的ID與名稱
    
    
    # 新增一個方法判斷借書時間是否過期
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


# 創建作者資料庫模型
class Author(models.Model):
    first_name = models.CharField('姓氏', max_length=100)
    last_name = models.CharField('名字', max_length=100)
    date_of_birth = models.DateField('出生日期', null=True, blank=True)
    date_of_death = models.DateField('死亡日期', null=True, blank=True)
    
    class Meta:
        ordering = ['first_name', 'last_name']
        
        
    def __str__(self):
        return f'{self.first_name}{self.last_name}'

    # 從資料庫呼叫時會回傳一個獨特有的url導向author-detail頁面，args值是回傳id得以在url展是獨特性的象徵。
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    

    
    
# 創建語言資料庫模型
class Language(models.Model):
    name = models.CharField('語言', max_length=50, help_text='請輸入書本所擁有的語言')
    
    def __str__(self):
        return self.name
    


    


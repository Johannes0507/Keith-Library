from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language


class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'id')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


# 把BookInstance設製成一個class
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'id')
    inlines = [BookInstanceInline] # 讓Book的新增頁面多了BookInstance的選項。



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'imprint', 'id', 'status')
    list_filter = ('status', 'due_back')

    
    
    fieldsets = (
    (None, {
        'fields': ('book','imprint', 'id')
    }),
    ('狀態', {
        'fields': ('status', 'due_back', 'borrower')
    }),
)






admin.site.register(Genre)

admin.site.register(Language)
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:44:36 2023

@author: KeithLee
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 主頁
    path('books', views.BookListView.as_view(), name='books'), # 所有書籍
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), # 書本細節
    path('authors', views.AuthorListView.as_view(), name='authors'), # 所有作者
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'), # 作者細節
    ]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserView.as_view(), name='my-borrowed'), # 使用者租借出去的書
    ]

urlpatterns += [
    path('borrowed/', views.LibraryStaffPermissionView.as_view(), name='all-borrowed'), # 所有租借出去的書 
    ]

urlpatterns += [
    path('book/<uuid:pk>/renew', views.renew_book_librarian, name='renew-book-librarian'), # 修改租借時間
    ]

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'), # 創建作者
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'), # 更新作者
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'), # 刪除作者
]

urlpatterns += [
    path('boook/create/', views.BookCreate.as_view(), name='book_create'), # 創建書籍
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'), # 更新書籍
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'), # 刪除書籍
]
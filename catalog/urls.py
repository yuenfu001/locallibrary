from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='index'),
    path('books/', views.Books, name='book'),
    path('authors/', views.Authors, name='author'),
    path('book-details/<str:pk>/', views.BookInfo, name='bookinfo'),
    path('author-details/<str:pk>/', views.AuthorInfo, name='authorinfo'),
    path('fill-in-book/', views.Bookentry, name='bookform'),
    path('author-reg/', views.Register, name='authorform'),
    path('signup/', views.signUp, name='register'),
    path('signin/', views.log_in, name='login'),
    path('signout/', views.log_out, name='bye'),
]
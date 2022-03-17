from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from catalog.forms import BookForm
# from .forms import BookForm, RegFrom
from .forms import *
# from catalog.models import Author, Book, BookInstance, Genre
# Create your views here.

def home(request):
    book = Book.objects.all()
    author = Author.objects.all()
    copy = BookInstance.objects.all()
    genre = Genre.objects.all()
    num_book = book.count()
    num_authors = author.count()
    num_copy = copy.count()
    available_copy = copy.filter(status__iexact= 'a').count()

    context = {
        'book_num': num_book,
        'authors' : num_authors,
        'copy_num':num_copy,
        'copies_avail': available_copy
    }
    return render(request,'home.html', context)

def Books(request):
    books = Book.objects.all()
    context = {
        'all_book': books
    }
    return render(request, 'books.html',context)

def Authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html',{'all_author':authors})

def BookInfo(request,pk):
    
    books = Book.objects.all()
    book = books.get(id=pk)
    context = {
        'specific_book':book,
        
    }
    return render(request, 'book_info.html',context)

def AuthorInfo(request,pk):
    authors = Author.objects.all()
    author = authors.get(id=pk)
    authored = author.book_set.all()
    context = {
        'get_author':author,
        'books':authored,
    }
    return render(request, 'author_info.html',context)
@login_required(login_url='login')
def Bookentry(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    context = {
        'forms':form
    }
    return render(request, 'forms/bookform.html', context)

@login_required(login_url='login')
def Register(request):
    authform = RegFrom()
    if request.method == 'POST':
        authform = RegFrom(request.POST)
        if authform.is_valid():
            authform.save()
            return redirect('author')
    context = {
        'author':authform
    }
    return render(request, 'forms/authreg.html',context)

def signUp(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        signup = SignupForm()
        context = {
            'signform':signup
        }
        if request.method == 'POST':
            signup = SignupForm(request.POST)
            if signup.is_valid():
                signup.save()
                return redirect('login')

        return render(request,'account/register.html', context)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == 'POST':
            usern = request.POST.get('username')
            passw = request.POST.get('password')
            user = authenticate(request, username=usern, password=passw)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request, 'username or password is incorrect')

        context = {
        }
        return render(request, 'account/login.html', context)

def log_out(request):
    logout(request)
    return redirect('login')

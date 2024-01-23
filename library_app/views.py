from django.shortcuts import render, redirect
from django.contrib import messages
from .models import registration_table, Book
# for islowercase.. removing case sensivity
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        # input value
        author = request.POST.get('author_name')
        if author:
            obj = Book.objects.filter(Q(Author__iexact=author))
            return render(request, 'index.html', {"objects":obj})
        else:
            obj = Book.objects.all()
            return render(request, 'index.html', {"objects":obj})
    obj = Book.objects.all()
    return render(request, 'index.html', {"objects":obj})

# registration
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username:
            messages.error(request, 'Username is required.')
            return redirect('library_app:register')
        if registration_table.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists..')
            return redirect('library_app:register')
        elif registration_table.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exists..')
            return redirect('library_app:register')
        else:
            obj = registration_table.objects.create(username=username, email=email, password=password)
            obj.save()
            if obj:
                return redirect('library_app:login')
            else:
                messages.error(request, 'Authentication failed.')
                return redirect('library_app:register')
    return render(request, 'register.html')

# login
def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = registration_table.objects.filter(email=email, password=password)
        if user:
            return redirect('library_app:index')
        else:
            messages.error(request, 'Email or Password is invalid.')
    return render(request, 'login.html')

# create user
def create_book(request):

    if request.method == 'POST':
        book_name = request.POST.get('book')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description')

        if book_name and author and price:
            obj = Book.objects.create(Book_Name = book_name, Author = author, Price = price, Description= description)
            obj.save()
        else:
            return render(request, 'create_book.html')

    
    return render(request, 'create_book.html')

def delete(request, id):
    delete_item = Book.objects.filter(id = id)
    delete_item.delete()
    return redirect('library_app:index')
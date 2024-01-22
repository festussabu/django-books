from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username:
            messages.error(request, 'Username is required.')
            return redirect('library_app:register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists..')
            return redirect('library_app:register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exists..')
            return redirect('library_app:register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, is_active=True)
            
            authenticated_user = authenticate(username=username, password=password)
            
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Successfully Logged In...')
                return redirect('library_app:index')
            else:
                messages.error(request, 'Authentication failed.')
                return redirect('library_app:register')

    return render(request, 'register.html')


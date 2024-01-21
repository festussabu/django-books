from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def sign_up(request):
  return render(request, 'signUp.html')

def log_in(request):
  return render(request, 'logIn.html')
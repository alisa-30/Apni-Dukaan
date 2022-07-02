from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms  import UserRegisterForm


def index(request):
       return render(request,'index.html')

def log_in(request):
        return render( request, 'login.html')
def contact(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(index)
    else:
        form = UserRegisterForm()
    return render(request, 'contact.html', {'form': form})

def contacts(request):
    return render(request,'contacts.html')

# Create your views here.


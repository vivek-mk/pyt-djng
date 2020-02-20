from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        "title": "Helloo World!!!",
        "content": "Welcome to home page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    # contact_form = ContactForm()
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact DETails",
        "content": "Welcome to contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def about_page(request):
    context = {
        "title": "about DetAILS",
        "content": "Welcome to about page"
    }
    return render(request, "home_page.html", context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/login")
            else:
                return render(request, 'auth/login.html', {'error': 'Authentication error'})
    else:
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, 'auth/register.html', {})

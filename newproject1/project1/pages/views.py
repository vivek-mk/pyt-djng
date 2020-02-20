from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello</h1>") #string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123123,
        "my_list": [123, 345, 567, 312, "Abc"]
    }
    # return render(request,"about.html",{})
    return render(request, "about.html", my_context)

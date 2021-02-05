from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Value for the context key, lol"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About content goes here"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "This is a contact form",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if request.method == "POST":
        print(request.POST.get("Fullname"))
        print(request.POST.get("email"))
        print(request.POST.get("content"))
    return render(request, "contact/view.html", context)

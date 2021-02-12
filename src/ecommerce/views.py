from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    print(request.session.get("first_name", "Unknown"))
    context = {
        "title": "Value for the context key, lol",
        "content": "Welcome to the home page",
        "premium_content": "Welcome to the premium content",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "This is subscriber premium content"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About content goes here"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact us",
        "content": "Welcome to the contact page",
        "form": contact_form,
        # "brand": "New Brand Name, like Nike",
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get("Fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # redirect to a success page
            # context["form"] = LoginForm()
            return redirect("/")
        else:
            # return invalid login message
            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect("/")
    return render(request, "auth/register.html", context)

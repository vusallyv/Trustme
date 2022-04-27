from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")


def faq(request):
    return render(request, "faq.html")


def about_us(request):
    return render(request, "about-us.html")

def careers(request):
    return render(request, "careers.html")


def contact(request):
    return render(request, "contact.html")
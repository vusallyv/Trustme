from django.shortcuts import render

# Create your views here.

def blogs(request):
    return render(request, "blogs.html")


def blog_detail(request):
    return render(request, "blog-detail.html")

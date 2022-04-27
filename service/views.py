from django.shortcuts import render

# Create your views here.

def brief(request):
    return render(request, "brief.html")


def design_service(request):
    return render(request, "design-service.html")


def digital_audit(request):
    return render(request, "digital-audit.html")


def digital_strategy_service(request):
    return render(request, "digital-strategy-service.html")


def one_project(request):
    return render(request, "one-project.html")


def packets(request):
    return render(request, "packets.html")


def portfolio(request):
    return render(request, "portfolio.html")


def seo_service(request):
    return render(request, "seo-service.html")


def services(request):
    return render(request, "services.html")


def smm_service(request):
    return render(request, "smm-service.html")


def vacancy(request):
    return render(request, "vacancy.html")

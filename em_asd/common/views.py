from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def home_page(request):
    context = {}
    return render(request, 'common/home_page.html', context)


def about(request):
    context = {}
    return render(request, 'common/about.html', context)


@login_required
def compressors(request):
    context = {}
    return render(request, 'common/compressors.html', context)


@login_required
def generators(request):
    context = {}
    return render(request, 'common/generators.html', context)


@login_required
def oil_separators(request):
    context = {}
    return render(request, 'common/oil_separators.html', context)

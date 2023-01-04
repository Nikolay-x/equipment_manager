import logging

from django.http import HttpResponse
from django.shortcuts import render


def page_not_found_view(request, exception=None):
    resp = HttpResponse
    logging.error(f'Server error appeared for {request.path}; method- {request.method}; response content- {resp}')
    return render(request, 'common/custom_error_page.html', status=404)


def error_view(request, exception=None):
    resp = HttpResponse
    logging.error(f'Server error appeared for {request.path}; method- {request.method}; response content- {resp}')
    return render(request, 'common/custom_error_page.html', status=500)


def permission_denied_view(request, exception=None):
    resp = HttpResponse
    logging.error(f'Server error appeared for {request.path}; method- {request.method}; response content- {resp}')
    return render(request, 'common/custom_error_page.html', status=403)


def bad_request_view(request, exception=None):
    resp = HttpResponse
    logging.error(f'Server error appeared for {request.path}; method- {request.method}; response content- {resp}')
    return render(request, 'common/custom_error_page.html', status=400)

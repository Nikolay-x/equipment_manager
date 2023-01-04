from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def check_if_engineer(request):
    return list(request.user.groups.filter(name__in=['Engineer']))

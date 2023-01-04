from django.shortcuts import render


def allow_groups(groups=None):
    if groups is None:
        groups = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return render(request, 'common/access_denied.html')

            if request.user.is_superuser or not groups:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.filter(name__in=groups)

            if not user_groups:
                return render(request, 'common/access_denied.html')

            return view_func(request, *args, **kwargs)

        return wrapper

    if callable(groups):
        func = groups
        groups = []
        return decorator(func)

    return decorator

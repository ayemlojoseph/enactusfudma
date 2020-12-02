from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fuc):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return view_fuc(request, *args, **kwargs)
    return wrapper_func

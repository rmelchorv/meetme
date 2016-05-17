from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import auth

# Create your views here.


def index(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'meetme/index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('meetme:index', args=()))
        else:
			return render(request,'registration/login.html', {
                'error_message': "The password is valid, but the account has been disabled!",
            })
			return HttpResponse("Error1")
    else:
		return render(request, 'registration/login.html', {
			'error_message': "The username and password were incorrect.",
		})

def logout(request):
    return auth.views.logout_then_login(request)
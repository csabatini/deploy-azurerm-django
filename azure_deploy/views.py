from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from azure_ad_auth.utils import get_logout_url


def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    redirect_uri = request.build_absolute_uri(reverse_lazy('azure_complete'))
    logout_url = get_logout_url(redirect_uri)
    return HttpResponseRedirect(logout_url)

def success(request):
    return render(request, 'registration/login_success.html')

def subs(request):
    state = request.session['state']
    nonce = request.session['nonce']
    code = request.session['code']
    token = request.session['token']
    return render(request, 'subscriptions.html', {'state': state, 'nonce': nonce, 'code': code, 'access_token': token})

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from azure_ad_auth.utils import get_logout_url
from django.contrib.auth.decorators import login_required
import requests, json

from .models import JSONFile
from .forms import JSONFileForm


def index(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    redirect_uri = request.build_absolute_uri(reverse('logout_complete'))
    logout_url = get_logout_url(redirect_uri)
    return HttpResponseRedirect(logout_url)


@login_required
def subs(request):
    SUB_URL='https://management.azure.com/subscriptions'
    access_token = request.session['access_token']
    headers = {'Authorization': 'bearer %s' % (access_token)}
    params={'api-version': '2015-06-01-preview'}
    r = requests.get(SUB_URL, headers=headers, params=params)
    data = json.loads(r.text)
    return render(request, 'subscriptions.html', data)

@login_required
def templates(request):
    form = JSONFileForm()
    if request.method == 'POST':
        print 'this should handle the post'

    files = JSONFile.objects.all()

    return render(request, 'templates.html', {'files': files, 'form': form})


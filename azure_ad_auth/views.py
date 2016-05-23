from .backends import AzureActiveDirectoryBackend
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import requests
import urlparse
import uuid
import json

@never_cache
def auth(request):
    backend = AzureActiveDirectoryBackend()
    redirect_uri = request.build_absolute_uri(reverse(complete))
    nonce = str(uuid.uuid4())
    request.session['nonce'] = nonce
    state = str(uuid.uuid4())
    request.session['state'] = state
    login_url = backend.login_url(
        redirect_uri=redirect_uri,
        nonce=nonce,
        state=state
    )
    return HttpResponseRedirect(login_url)


@never_cache
@csrf_exempt
def complete(request):
    backend = AzureActiveDirectoryBackend()
    redirect_uri = request.build_absolute_uri(reverse(complete))
    method = 'GET' if backend.RESPONSE_MODE == 'fragment' else 'POST'
    original_state = request.session.get('state')
    state = getattr(request, method).get('state')
    if original_state == state:
        code = getattr(request, method).get('code')
        nonce = request.session.get('nonce')
        if code is not None:
            data = backend.token_params(
                redirect_uri=redirect_uri,
                code=code,
            )
            url = data.pop('endpoint', None)
            token_response = requests.post(url, data=data)
            payload = json.loads(token_response.text)
            id_token = payload['id_token']
            request.session['access_token'] = payload['access_token']
            request.session['code'] = code
            user = backend.authenticate(token=id_token, nonce=nonce)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(get_login_success_url(request))

    return HttpResponseRedirect('failure')


def get_login_success_url(request):
    redirect_to = request.GET.get(REDIRECT_FIELD_NAME, '')
    netloc = urlparse.urlparse(redirect_to)[1]
    if not redirect_to:
        redirect_to = settings.AAD_REDIRECT_URL
    elif netloc and netloc != request.get_host():
        redirect_to = settings.AAD_REDIRECT_URL
    return redirect_to

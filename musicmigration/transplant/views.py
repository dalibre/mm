from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from transplant import getSpotifyCredentials


def index(request):
    cid, secret, red_url = getSpotifyCredentials()
    return render(request, 'index.html', {'cid': id, 'secret': secret,
                                          'red_url': red_url})

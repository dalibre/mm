from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from transplant.spotifyfun import getSpotifyCredentials

import spotipy
import spotipy.util as util


def index(request):
    cid, secret, red_url = getSpotifyCredentials()
    return render(request, 'transplant/index.html', {'cid': cid, 'secret': secret,
                                          'red_url': red_url})

def spotify_auth(request):
    scope = 'user-follow-read'
    util.prompt_for_user_token()
    cid, secret, red_url = getSpotifyCredentials()

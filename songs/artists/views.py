
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .models import Artist
"""
songs=[
    {
    "id":0,
    "name":"Stranger",
    "singer":"Dimash Kudaibergen"
},

  {
    "id":1,
    "name":"Timi Nai Hau",
    "singer":"Sabin Rai "
},
  {
    "id":2,
    "name":"Herda Herdai",
    "singer":"Raju Lama"
},
{
    "id":3,
    "name":"Darshan Namaste",
    "singer":"Rajesh Payal Rai"
},

{
    "id":4,
    "name":"Timi Chhau",
    "singer":"Bishal Rai"
},


]
"""

def home(request):
    data = {'songs': Artist.objects.all()}
    return render(request, 'home.html', data)
   




def song(req):
    data = {'songs':Artist.objects.all()}
    return render(req, 'show.html', data)



def contact(req):
    return render(req, 'contact.html')


def show(req,id):
    #song=get_object_or_404(Artist.objects.all(), pk=id)
    #song=[s for s in songs if s["id"]==id]
    #return render(req, 'show.html', {"song":song})
    song=get_object_or_404(Artist, pk=id)
    return render(req, 'artist.html', {"artist":song})


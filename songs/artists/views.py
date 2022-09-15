
from django.http import HttpResponse
from django.shortcuts import render

#from .models import Animal
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

def home(request):
    return render(request, 'home.html', {"songs":songs})




def song(req):
    data = {'songs':songs}
    return render(req, 'artist.html', data)



def contact(req):
    return render(req, 'contact.html')


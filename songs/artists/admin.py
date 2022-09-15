from django.contrib import admin

from .models import Artist, ArtistType

# Register your models here.

admin.site.register(Artist)
admin.site.register(ArtistType)

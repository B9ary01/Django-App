from django.db import models

class ArtistType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Artist(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()
    type=models.ForeignKey(ArtistType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

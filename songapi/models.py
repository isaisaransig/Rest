from django.db import models

class Song(models.Model):
    ID_SONG = models.IntegerField()
    SONG_NAME = models.CharField(max_length=100)
    SONG_PATH = models.CharField(max_length=100)
    PLAYS = models.IntegerField()
    

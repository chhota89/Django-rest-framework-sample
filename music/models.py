# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 120)
    album_title = models.CharField(max_length = 120)

    def __str__(self):
        return  self.artist + " - "+self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    song_name = models.CharField(max_length = 120)
    file_type = models.CharField(max_length = 120)

    def __str__(self):
        return  self.song_name + " - "+self.file_type
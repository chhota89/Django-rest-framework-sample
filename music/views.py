# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
from  django.template import loader
from rest_framework.response import Response
from music.serializer import AlbumSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from music.serializer import AlbumSerializer
# Create your views here.
def index(request):
    all_album = Album.objects.all()
    # html = ''
    # for album in all_album:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href=' + url + '>' + album.album_title +'</a></br>'

    template = loader.get_template('music/index.html')
    context = {
        'all_album' : all_album,
    }
    return HttpResponse(template.render(context,request))

def details(request, album_id):
    return HttpResponse("<H2>Details for Album id "+ str(album_id) + "</H2>")

@api_view(['GET'])
def rest(request):
    all_album = Album.objects.all()
    serializer = AlbumSerializer(all_album, many=True)
    return Response(serializer.data)

class ListDemoClass(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class DeatailsView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class UpdateApiView(UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class DestroyApiVIew(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    
class CreateApi(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    
    
    
    

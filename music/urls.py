from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),

    # /music/322/
    url(r'^(?P<album_id>[0-9]+)/$',views.details , name = 'details'),

    url(r'^rest/', views.rest, name='rest'),

    url(r'^album/', views.ListDemoClass.as_view(), name='list_class'),

    url(r'^(?P<pk>[\w-]+)/details/$', views.DeatailsView.as_view(), name='details'),

    url(r'^(?P<pk>[\w-]+)/update/$', views.UpdateApiView.as_view(), name='update'),
    
    url(r'^(?P<pk>[\w-]+)/delete/$', views.DestroyApiVIew.as_view(), name='delete'),
    
    url(r'^create/', views.CreateApi.as_view(), name='create'),


]
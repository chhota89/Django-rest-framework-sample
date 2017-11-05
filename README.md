
install the django
easy_install django

check the django version
django-admin --version

create new project
django-admin startproject project_name

Run server
python manage.py runserver

create new app
python mage.py startapp app_name

To resolve migration(Change the data base )
python manage.py migrate

creating the new model migrations
python manage.py makemigrations music (music is app name) (After this do again migrate)

to see the sql query for models 
python manage.py sqlmigrate music 0001   (0001 is migration number genrated by python)

to start the django power shell
python manage.py shell

-------------------------------------------------------------------------------------------------------
power shell practice
from music.models import Album,Song  (music is app name, models is file name, Album and Song is the class name)
>>> a = Album(artist = "mohmad", album_title = "Dhin dhin")
>>> a.save()
>>> a.artist

>>> Album.objects.all()
<QuerySet [<Album: mohmad Dhin dhin>, <Album: ismail jslk>]>
>>> Album.objects.filter(id = 1)
<QuerySet [<Album: mohmad Dhin dhin>]>
>>> Album.objects.filter(artist = "mohmad")
<QuerySet [<Album: mohmad Dhin dhin>]>

---------------------------------------------------------------------------------------------------------------

createing the database user
python manage.py  createsuperuser





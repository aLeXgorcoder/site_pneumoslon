from django.contrib import admin
from .models import Concert, Album, Song

admin.site.register(Concert)
admin.site.register(Album)
admin.site.register(Song)

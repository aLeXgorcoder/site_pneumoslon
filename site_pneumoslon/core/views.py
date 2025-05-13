from django.shortcuts import render
from .models import Album

def index(request):
    data = Album.objects.all()  # Получение всех записей из модели
    return render(request, 'core/index.html', {'data': data})
# # from django.shortcuts import render

# # # Create your views here.
# from django.http import HttpResponse # type: ignore


# def index(request):
#     return HttpResponse('<h1>Здесь же была ракета!</h1>')

from django.http import HttpResponse
from django.conf import settings
# from django.shortcuts import render
import os


def index(request):
    image_path = os.path.join(settings.MEDIA_ROOT, 'your_image.jpg')
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
    return response

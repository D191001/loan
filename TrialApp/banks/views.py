# from django.shortcuts import render
from django.http import HttpResponse


def show_image(request):
    image_path = 'media/1.jpg'
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
        return response

import os

from django.conf import settings
from django.http import HttpResponse


def index(request):
    image_path = os.path.join(settings.MEDIA_ROOT, 'your_image.jpg')
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
    return response

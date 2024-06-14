import os

from django.conf import settings
from django.http import HttpResponse


def index(request):
    media_root = settings.MEDIA_ROOT
    image_path = os.path.join(media_root, '1.jpg')
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
    return response

# from django.shortcuts import render
from django.http import HttpResponse


def show_image(request):
    # media_root = settings.MEDIA_ROOT
    # image_path = os.path.join(media_root, '1.jpg')
    image_path = 'media/1.jpg'
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
        # response['Content-Disposition'] = 'attachment; filename="1.jpg"',
        return response

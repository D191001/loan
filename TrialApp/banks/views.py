# from django.http import HttpResponse


# def show_image(request):
#     image_path = 'media/2.jpg'
#     with open(image_path, 'rb') as f:
#         response = HttpResponse(f.read(), content_type='image/jpeg')
#         return response


from django.shortcuts import render


def index(request):
    return render(request, "index.html")

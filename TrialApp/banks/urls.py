# from django.urls import path

# from . import views

# urlpatterns = [
#     # path('', views.index),
#     path('', views.show_image, name='show_image'),
# ]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]

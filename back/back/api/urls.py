from django.urls import include, path
from .views import *
urlpatterns = [
    path('products', ProductAPIViw.as_view()),
    path('products/<int:pk>', ProductAPIViw.as_view()),

    path('trash', ProductAPIViw.as_view()),
    path('trash/<int:pk>', ProductAPIViw.as_view()),
]

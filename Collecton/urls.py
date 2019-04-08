from django.urls import path

from .views import webpage

urlpatterns = [
    path('', webpage, name='home')
]

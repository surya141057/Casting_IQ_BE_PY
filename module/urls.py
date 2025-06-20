from django.urls import path
from .views import *

urlpatterns = [
    path('api/module/', moduleView.as_view(), name='module'),
]
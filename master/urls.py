# castingiq/urls.py (main project urls)
from django.urls import path
from .views import pattern_typeView

urlpatterns = [
    path('api/pattern-type/', pattern_typeView.as_view(), name='pattern-type'),
]
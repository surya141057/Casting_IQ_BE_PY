"""
URL configuration for castingiq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from master.views import pattern_typeView
from module.views import ModuleView
from master.views import matchPlate_typeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pattern-type/', pattern_typeView.as_view(), name='pattern-type'),
    path('api/module/', ModuleView.as_view(), name='module'),
    path('api/matchPlate-type/', matchPlate_typeView.as_view(), name='matchPlate_type'),
    path('api/module/', ModuleView.as_view(), name='module'),
]

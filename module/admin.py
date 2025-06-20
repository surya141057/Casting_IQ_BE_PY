# module/admin.py

from django.contrib import admin
from .models import Module, SubModule  # Import your models from the same app

# Register the Module and SubModule models
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']  # Customize what fields to display

@admin.register(SubModule)
class SubModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'module', 'description']  # Display related module

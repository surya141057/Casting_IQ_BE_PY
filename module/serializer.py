from module.models import SubModule,Module
from rest_framework import serializers

class sub_moduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubModule
        fields = ['name']
        
class ModuleWithSubmodulesSerializer(serializers.ModelSerializer):
    submodules = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ['name', 'submodules']

    def get_submodules(self, obj):
        return [submodule.name for submodule in obj.submodule_set.all()]
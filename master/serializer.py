from master.models import *
from utils.codeAutoGenerate import CodeAutoGenerate
from rest_framework import serializers


class pattern_typeSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False, error_messages={'invalid': 'Is Active must be True or False'.capitalize().replace('_', ' ')}, default=True)
    
    class Meta:
        model = pattern_type
        fields = ('id','code','name', 'description', 'notes', 'is_active', 'is_draft')

    def validate(self, attrs):
        instance_id = getattr(self.instance, 'id', None)    
        return CodeAutoGenerate.generate_code(self.Meta.model, attrs, prefix='EMT', id=instance_id)

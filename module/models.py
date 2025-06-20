from common.models import BaseModel
from django.db import models

class Module(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name    
class SubModule(BaseModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        unique_together = ('module', 'name')
    def __str__(self):
        return f"{self.module.name} -> {self.name}"
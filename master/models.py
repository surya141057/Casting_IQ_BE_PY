from django.db import models
from common.models import BaseModel

class pattern_type(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class matchPlate_type(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
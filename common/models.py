from django.db import models
class BaseModel(models.Model):
    created_by = models.CharField(max_length=32, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=32, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_draft = models.BooleanField(default=False)
    notes = models.CharField(max_length=150, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
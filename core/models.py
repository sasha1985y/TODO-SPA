from django.db import models
import uuid

class Todo(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=32, unique=True, default=uuid.uuid4().hex)

    def __str__(self):
        return self.name
    

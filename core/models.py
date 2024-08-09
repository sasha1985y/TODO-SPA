from django.db import models
import uuid

def generate_unique_id():
    return uuid.uuid4().hex

class Todo(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=32, unique=True, default=generate_unique_id)

    def __str__(self):
        return self.name
    

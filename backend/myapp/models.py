from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"name {self.name} email {self.email} created_at {self.created_at}"
    
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    introduce = models.TextField()
    created_by = models.CharField(max_length=18)
    
    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField(blank=False)
    image = models.ImageField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title


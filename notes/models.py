from django.db import models
from django.contrib.auth.models import User



class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=26)
    description = models.CharField(max_length=1000,default='')
    genre = models.CharField(max_length=26,default='')
    image = models.FileField(upload_to='user_files/', null=True, blank=True)
    year = models.CharField(max_length=4,default='')
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(6)])  # Adjusted rating field to be out of 5
    created = models.DateField(auto_now_add=True)

    

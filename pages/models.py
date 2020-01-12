from django.db import models

# Create your models here.

class Pages(models.Model):
    text = models.TextField()
    #timne = models.TimeField()
    #response = models.CharField()

        
    def __str__(self): 
        return self.text
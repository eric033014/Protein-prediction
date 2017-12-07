from django.db import models

class Profile(models.Model):
    user_name = models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    comment=models.FileField(max_length=5000)
    def __unicode__(self):
        return self.name
# Create your models here.

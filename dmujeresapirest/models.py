from django.db import models

class Client(models.Model):
    name = models.TextField()
    lastname = models.TextField()
    identification = models.TextField()
    telephone = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.

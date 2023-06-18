from django.db import models

# Create your models here.
class thoughts(models.Model):
    Pers_name=models.CharField(max_length=255)
    comment=models.TextField()

    def __str__(self):
        return self.Pers_name
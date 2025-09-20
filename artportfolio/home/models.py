from django.db import models

# Create your models here.
class PortfolioImage(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=75)
    media = models.ImageField(upload_to='art/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
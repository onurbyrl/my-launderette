from django.db import models

# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(blank=True)
    importance = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
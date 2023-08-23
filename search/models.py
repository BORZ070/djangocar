from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='manager_photo')
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

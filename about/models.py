from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='manager_photo')
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=500, blank=True, null=True)
    manager_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
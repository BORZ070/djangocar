from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

class Manufacture(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class Body(models.Model):
    body_type = models.CharField(max_length=50)

    def __str__(self):
        return self.body_type


class Transmission(models.Model):
    transmission_type = models.CharField(max_length=50)

    def __str__(self):
        return self.transmission_type


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    generation = models.CharField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='car_image', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='car_image', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='car_image', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='car_image', blank=True, null=True)

    brand_name = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.PROTECT)
    manufacture = models.ForeignKey(Manufacture, blank=True, null=True, on_delete=models.PROTECT)
    body = models.ForeignKey(Body, blank=True, null=True, on_delete=models.PROTECT)
    transmission = models.ForeignKey(Transmission, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} // {self.brand}'





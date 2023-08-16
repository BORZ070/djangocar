from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    generation = models.CharField(max_length=50)
    info = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='car_image', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='car_image', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='car_image', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='car_image', blank=True, null=True)


    def __str__(self):
        return f'{self.id} // {self.brand}'


# class Manufacture(models.Model):
#     country = models.CharField(max_length=50)

# class Body(models.Model):
#     body_type = models.CharField(max_length=50)

# class Transmision(models.Model):
#     transmision_type = models.CharField(max_length=50)

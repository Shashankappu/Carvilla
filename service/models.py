from django.db import models

class Feedback(models.Model):
    user_image = models.CharField(max_length=50)
    feedback = models.TextField()
    name = models.CharField(max_length=10)
    place = models.CharField(max_length=50)

class Featuredcars(models.Model):
    car_name = models.CharField(max_length=20)
    car_price = models.IntegerField()
    car_image_url = models.CharField(max_length=100)
    car_model = models.CharField(max_length=4)
    car_hp = models.CharField(max_length=8)
    car_type = models.CharField(max_length=10)
    car_odometer_reading = models.CharField(max_length=8)
    car_description = models.TextField()
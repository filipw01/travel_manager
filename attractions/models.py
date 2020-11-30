from django.db import models


class City(models.Model):
    class Meta:
        verbose_name_plural = "cities"
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    attractions = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    image = models.CharField(max_length=256)

    def __str__(self):
        return self.name

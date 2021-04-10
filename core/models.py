from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class CarSeat(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='seats'
    )
    number = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.car.name} - {self.number}'


class Ticket(models.Model):
    seat = models.ForeignKey(
        CarSeat,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    departure_at = models.DateTimeField()
    departure_city = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

    def __str__(self):
        available_msg = 'available.' if self.available else 'unavailable!'
        return f'{self.seat} is {available_msg}'


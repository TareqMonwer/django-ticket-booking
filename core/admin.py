from django.contrib import admin
from .models import Car, CarSeat, Ticket


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(CarSeat)
class CarSeatAdmin(admin.ModelAdmin):
    list_display = ['car', 'number']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'seat',
        'departure_at',
        'departure_city',
        'available'
    ]

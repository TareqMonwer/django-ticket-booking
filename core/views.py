import datetime as dt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Ticket, CarSeat, Car


def home(request):
    return render(request, 'core/index.html')


def seat_planner(request):
    car = Car.objects.get(id=1)
    seats = CarSeat.objects.filter(car=car)
    departure_city = request.GET.get('from')
    destination = request.GET.get('to')

    if request.method == 'GET':
        departure_city = request.GET.get('from')
        destination = request.GET.get('to')
        departure_date = request.GET.get('date')
        departure_time = request.GET.get('time')
        departure_time = dt.datetime(
            *list(map(int, departure_date.split('-'))),
            *list(map(int, departure_time.split('.')))
        )
        request.session['booking_time'] = departure_time.strftime(
            '%Y-%m-%d %H.%M'
        )
        booked_tickets = Ticket.objects.filter(
            departure_at=departure_time,
            departure_city__iexact=departure_city
        )
        booked_seats = [ticket.seat for ticket in booked_tickets]
        ctx = {
            'seats': seats,
            'booked_seats': booked_seats,
            'departure_city': departure_city,
            'destination': destination
        }
        print(booked_tickets)
        return render(request, 'core/seats.html', ctx)

    elif request.method == 'POST':
        seats = set(request.POST.getlist('seats'))
        from_city = request.POST.get('from_city').lower()
        to_city = request.POST.get('to_city').lower()

        for seat in seats:
            seat = CarSeat.objects.get(car=car, number=seat)
            dept_time = dt.datetime.strptime(
                request.session['booking_time'],
                '%Y-%m-%d %H.%M'
            )
            Ticket.objects.create(
                seat=seat,
                departure_at=dept_time,
                departure_city=from_city
            )
            # del request.session['booking_time']
        msg = ', '.join(seats) + ' You booked these seats.'
        return HttpResponse(msg)


def pay(request):
    return Response('PAID..')

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def seat_planner(request):
    return render(request, 'core/seats.html')


def pay(request):
    if request.method == 'POST':
        seats = request.POST.getlist('seats')
        msg = ', '.join(seats) + ' You booked these seats.'
        return HttpResponse(msg)

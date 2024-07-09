from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from room.models import Room, Booking

@login_required
def dashboard(request):
    total_rooms = Room.objects.count()
    available_rooms = Room.objects.filter(is_available=True).count()
    booked_rooms = total_rooms - available_rooms
    total_bookings = Booking.objects.count()

    context = {
        'total_rooms': total_rooms,
        'available_rooms': available_rooms,
        'booked_rooms': booked_rooms,
        'total_bookings': total_bookings,
    }
    return render(request, 'dashboard/dashboard.html', context)

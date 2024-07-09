from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import *

def add_category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New category added to manage rooms ")
            return redirect('add-category')
        else:
            messages.warning(request, "Something went wrong. please check for inputs")
            return redirect('add-category')
    else:
        form = AddCategoryForm()
        context = {'form':form, 'category':category}
    return render(request, 'room/add-category.html', context)

def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = UpdateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category information updated and saved")
            return redirect(reverse('update-category', args=[category.pk]))
        else:
            messages.warning(request, "Somethin went wrong. please check for errors")
            return redirect(reverse('update-category', args=[category.pk]))
    else:
        form = UpdateCategoryForm(instance=category)
        context = {'form':form, 'category':category, 'categories':categories}
    return render(request, 'room/update-category.html', context)

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    messages.success(request, "Category is now deleted")
    return redirect('dashboard')
            
def add_room(request):
    room = Room.objects.all()[:5]
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New room information added and saved")
            return redirect('add-room')
        else:
            messages.warning(request, "Somethin went wrong. please check for errors")
            return redirect('add-room')
    else:
        form = AddRoomForm()
        context = {'form':form, 'room':room}
    return render(request, 'room/add-room.html', context)

def update_room(request, pk):
    rooms = Room.objects.get(pk=pk)
    room = Room.objects.all()
    if request.method == 'POST':
        form = UpdateRoomForm(request.POST, instance=rooms)
        if form.is_valid():
            form.save()
            messages.success(request, "Form info is now updated and saved")
            return redirect(reverse('update-room', args=[rooms.pk]))
        else:
            messages.warning(request, "Somethin went wrong. please check for errors")
            return redirect(reverse('update-room', args=[rooms.pk]))
    else:
        form = UpdateRoomForm(instance=rooms)
        context = {'form':form, 'rooms':rooms, 'room':room}
    return render(request, 'room/update-room.html', context)

def all_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'room/all-rooms.html', context)

def delete_room(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    messages.success(request, "Room has been deleted")
    return redirect('all-rooms')

def new_booking(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewBookingForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.room = room
            room.is_available = False
            var.save()
            room.save()
            messages.success(request, 'New booking has been made')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. please check')
            return redirect(reverse('new-booking', args=[room.pk]))
    else:
        form = NewBookingForm()
        context = {'room':room, 'form':form}
    return render(request, 'room/new-booking.html', context)

def update_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking info has been updated and save')
            return redirect(reverse('update-booking', args=[booking.pk]))
        else:
            messages.warning(request, 'Something went wrong. please check')
            return redirect(reverse('update-booking', args=[booking.pk]))
    else:
        form = UpdateBookingForm(instance=booking)
        context = {'form':form, 'booking':booking}
    return render(request, 'room/update-booking.html', context)

def checkout_guests(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.checkedout = True

    room = Room.objects.get(pk=booking.room.pk)
    room.is_available = True
    room.save()
    booking.save()
    messages.success(request, 'Guest has been checked out and room is now available for use..')
    return redirect('dashboard')

def guest_history_per_room(request, pk):
    room = Room.objects.get(pk=pk)
    guest = room.booking_set.all().order_by('checkedout')
    context = {'guest':guest, 'room':room}
    return render(request, 'room/guest-history-per-room.html', context)

def all_active_guests(request):
    guests = Booking.objects.filter(checkedout=False)
    context = {'guests':guests}
    return render(request, 'room/all-active-guests.html', context)

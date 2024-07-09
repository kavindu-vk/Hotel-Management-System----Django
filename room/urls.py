from django.urls import path
from . import views

urlpatterns = [
    path('add-category/', views.add_category, name='add-category'),
    path('update-category/<int:pk>/', views.update_category, name='update-category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete-category'),

    path('add-room/', views.add_room, name='add-room'),
    path('update-room/<int:pk>/', views.update_room, name='update-room'),
    path('all-rooms/', views.all_rooms, name='all-rooms'),
    path('delete-room/<int:pk>/', views.delete_room, name='delete-room'), 

    path('new-booking/<int:pk>/', views.new_booking, name='new-booking'),
    path('update-booking/<int:pk>/', views.update_booking, name='update-booking'),

    path('checkout-guest/<int:pk>/', views.checkout_guests, name='checkout-guest'),


    path('guest-history-per-room/<int:pk>/', views.guest_history_per_room, name='guest-history-per-room'),
    path('all-active-guests/', views.all_active_guests, name='all-active-guests'),
]
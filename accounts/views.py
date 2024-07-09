from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f"Welcome you are loged in as {user}")
            return redirect('dashboard')
        else:
            messages.warning(request, "Something went wrong! please check form input")
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Your active session is now ended, Log in to continue.")
    return redirect('login')


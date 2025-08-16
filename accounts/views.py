from django.shortcuts import render, redirect
from .models import HotelUser
from django.db.models import Q
from django.contrib import messages
from .utils import generateRandomToken , sendEmailToken

# Create your views here.
def login_page(request):
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":  
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        hotel_user = HotelUser.objects.filter(
            Q(email = email) | Q(phone_number = phone_number)
        )

        if hotel_user.exists():
            messages.error(request, "Account exists with Email or Phone Number.")
            return redirect('/account/register/')
        
        hotel_user = HotelUser.objects.create(
            username = phone_number,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            email_token =generateRandomToken()
        )
        hotel_user.set_password(password)
        hotel_user.save()
        sendEmailToken(email , hotel_user.email_token)

        messages.success(request, "Account exists with Email or Phone Number.")
        return redirect('/account/register/')

    return render(request, 'register.html')

def verify_email_token(request, token){
    hotel_user = 
}


from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pytz
from django.utils import timezone

# Create your views here.

def morning_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse("<h1> Hello Good Morning! Now the time is " + formatted_time + "</h1>")

def noon_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse("<h1> Hello Good Afternoon! Now the time is " + formatted_time + "</h1>")

def evening_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse("<h1> Hello Good Evening! Now the time is " + formatted_time + "</h1>")


def message(request):

    current_time_utc = timezone.now()

    ist_tz = pytz.timezone('Asia/Kolkata')
    current_time_ist = current_time_utc.astimezone(ist_tz)

    hour = current_time_ist.hour

    if 6 <= hour < 12:
        greeting_msg = "Hello Student!"
    elif 12 <= hour < 16:
        greeting_msg = "Hello, Good Afternoon!"
    elif 16 <= hour < 21:
        greeting_msg = "Hello, Good Evening!"
    elif 21 <= hour < 23:
        greeting_msg = "Hello, Good Night!"
    else:
        greeting_msg = "Hello, How are you?"

    formatted_time = current_time_ist.strftime("%d-%m-%Y %H:%M:%S")

    return HttpResponse(f"{greeting_msg} Today, the date and time in India is: {formatted_time}")

# Create your views here.
from django.http import HttpResponse
import datetime

# def display(request):
#     s = "<h1> Hello students, Welcome to Django Classes!/<h1>"
#     return HttpResponse(s)


def moringn_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%y %H:%M:%M:%S")
    return HttpResponse("<h1>Hello, Good MOrning! How are you today? NOw the time is: " + formatted_time + "</h1>")

def afternoon_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%y %H:%M:%M:%S")
    return HttpResponse("<h1>Hello, Good Afternnon! How are you today? NOw the time is: " + formatted_time + "</h1>")

def evening_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%y %H:%M:%M:%S")
    return HttpResponse("<h1>Hello, Good Evening! How are you today? NOw the time is: " + formatted_time + "</h1>")

# pip install pytz:
import pytz
from django.utils import timezone

def message(request):

    current_time_utc = timezone.now()
    ist_tz = pytz.timezone("Asia/Kolkata")
    current_time_ist = current_time_utc.astimezone(ist_tz)


    hour = current_time_ist.hour

    if 6 < hour < 12:
        greeting_msg = "Hello Students! Good Morning!"
    elif 12 <= hour <= 16:
        greeting_msg = "Hello Students! Good Afternoon!"
    elif 16 <= hour <= 21:
        greeting_msg = "Hello Students! Good Evening!"
    elif 21 <= hour <= 23:
        greeting_msg = "Hello Students! Good Night!"
    else:
        greeting_msg = "Hello, How are you?"


    forammatted_time = current_time_ist.strftime("%d-%m-%Y %H:%M:%S")

    return HttpResponse(f"{greeting_msg} today, the date and tim in India is: {forammatted_time}")
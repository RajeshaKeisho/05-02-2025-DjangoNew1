from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    time = datetime.datetime.now()
    name = "ABC"
    rollno = 101
    marks = 90
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    my_dict = {'insert_time':formatted_time, 'name':name, 'rollno':rollno, 'marks':marks}
    return render(request, 'wish.html', my_dict)

def wish1(request):
    time = datetime.datetime.now()
    msg = "Hello, friends!! very very good"
    h = int(time.strftime("%H"))
    if h<=12:
        msg += "Morning!"
    elif h<=16:
        msg += "Afternoon!"
    elif h<=21:
        msg += "Evening!"
    else:
        msg = "Hello, friends! good Night!"
    my_dict1 = {'insert_time':time, 'insert_data':msg}
    return render(request, 'myapp/wish1.html', context=my_dict1)

def greet(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%H %M %S")

    if now.hour < 12:
        greeting = "Good morning!"
    elif now.hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    return render(request, 'greet.html', {'greeting':greeting, 'current_time':current_time})

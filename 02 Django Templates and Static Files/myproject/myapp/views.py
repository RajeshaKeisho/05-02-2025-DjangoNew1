from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    time = datetime.datetime.now()
    name = 'ABC'
    rollno = 1001
    marks = 90

    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")

    my_dict = {"insert_time":formatted_time, 'name':name, 'rollno':rollno, 'marks':marks}

    return render(request, 'wish.html', my_dict)
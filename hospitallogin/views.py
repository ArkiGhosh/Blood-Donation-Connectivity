import string
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from hospitaldashboard.views import authenticatehospital

pin = ''

# Create your views here.
def hospitallogin(request):
    # global hospital_pin
    
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "regpin":
                pin = value
            
        
        c = "select * from hospital where PIN = '{}'".format(pin)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.warning(request, 'Incorrect credentials!')
        else:
            authenticatehospital(t[0][0])
            response = redirect('/hospitaldashboard/')
            return response

    return render(request,'hospitallogin.html')
      #fix
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from donordashboard.views import authenticate
email = ''
Pword = ''
# Create your views here.
def donorlogin(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "email":
                email = value
            if key == "password":
                Pword = value
        
        c = "select * from Donor where DonorEmail = '{}' and DonorPassword = '{}'".format(email,Pword)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.warning(request, 'Incorrect credentials!')
        else:
            authenticate(t[0][3])
            response = redirect('/donordashboard/')
            return response

    return render(request,'donorlogin.html')
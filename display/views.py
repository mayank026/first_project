from django import http
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import user_query,docs,medical_storesservice,laundry,library,laboratory
# Create your views here.

def home_page(request):
    if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            """value_con = {
            'name' :name,
            'email' :email ,
            'phone' :phone,
            }"""
            error_query =""
            if not name:
                error_query = "Enter your name"
            if not email:
                error_query = "Enter your email"
            if not phone:
                error_query = "Enter your contact number"
            if len(phone) < 10:
                error_query = "Enter a valid phone number"  
            if not message:
                error_query = "Enter your message!"
            if not error_query:                  
                query = user_query(user_name = name,user_email = email,user_number = phone,user_querry = message)
                query.save()
                messages.info(request,"Your message was sent, Thank you!")
                return redirect('/')
            else:
                datac ={
                'error_con' : error_query,
                #'values_con' : value_con
            }   
            return render(request,"display/index.html",datac)  

    return render(request,"display/index.html")


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # validation
        value = {
            'name' :name,
            'username' :username,
            'email' :email ,
        }
        agree = request.POST.get('agree-term','off')
        error_message = ""
        if not name:
            error_message = "Name required!!"
        elif len(name) < 3:
            error_message = "Name should be atleast of 3 characters!!"
        elif not username:
            error_message = "Username can't be blank!!"
        elif len(username) < 3:
            error_message = "Username should be atleast of 3 characters!!" 
        elif not email:
            error_message = "Email Required !!" 
        elif email[0]=='@':
            error_message = "invalid email address !!"
        elif not pass1:
            error_message = "Password Required !!"
        elif len(pass1) < 6:
            error_message = "Password can't be smaller than 6 characters!!"
        elif not pass2:
            error_message = "Confirm Password can't be blank!!"      
        

        if not error_message:
            if pass1==pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already in use!')
                    return redirect('/register/')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Your email id already exists!')
                    return redirect('/register/')
                else:        
                    if agree == "on":
                        user = User.objects.create_user(first_name=name,username=username, email=email,password = pass1)
                        user.save();
                        return redirect('/login/')
                    else:
                        messages.info(request,"Process can't be completed without agreeing to TERMS and CONDITIONS")
                        return redirect('/register/') 
                
            else:
                messages.info(request,"Password doesn't match") 
                return redirect('/register/')    
        else:
            data ={
                'error' : error_message,
                'values' : value
            }   
            return render(request,"display/register.html",data)      
           

    else:
        return render(request,"display/register.html") 


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not username:
            messages.info(request,"To log in, enter your username!")
            return redirect("/login/")
        elif not password:
            messages.info(request,"To log in, enter your password!")
            return redirect("/login/")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('/login/')    
    else:    
        return render(request,"display/login.html") 

def logout(request):
    auth.logout(request)
    return redirect('/')  

def about(request):
    return render(request,"display/aboutus.html") 


def message(request):
    return render(request,"display/message.html")              
print("1")
def doctors(request):
    
    if request.method == "GET":
        pincode = request.GET.get('pincode',"")
        city=request.GET.get('city',"")
        Physician = request.GET.get('Physician',"off")
        Dentist = request.GET.get('Dentist',"off")
        Gynaecologist = request.GET.get('Gynaecologist',"off")
        Eye= request.GET.get('Eye',"off")
        all_hostel_name = docs.objects.all()
        if pincode:
            all_hostel_name = all_hostel_name.filter(docs_pincode = pincode)
            if not all_hostel_name :
                return render(request,"display/pincode_not_found.html") 
        if Physician == "on":
            all_hostel_name = all_hostel_name.filter(docs_Physician=1)
        if Dentist == "on":
            all_hostel_name = all_hostel_name.filter(docs_Dentist=1)
        if Gynaecologist == "on":
            all_hostel_name = all_hostel_name.filter(docs_Gynaecologist=1)
        if Eye == "on":
            all_hostel_name = all_hostel_name.filter(docs_Eye=1)
        if Physician=="off" and Dentist=="off" and Gynaecologist=="off" and Eye=="off" and pincode=="":
            all_hostel_name = docs.objects.all()
        if city!='':
            all_hostel_name = all_hostel_name.filter(docs_city__exact = city)
        if not all_hostel_name:
            return render(request,"display/pincode_not_found.html")
        demo = {
                    'docs_list' : all_hostel_name,
                    'pincode': pincode,
                    'city': city
                }
        return render(request,"display/doctors.html",demo)
    else:
        all_hostel_name = docs.objects.all()
        demo2 = {
                'docs_list' : all_hostel_name,
        }
    return render(request,"display/doctors.html",demo2)


def medical_stores(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_medical_stores_name = medical_storesservice.objects.filter(medical_stores_pincode = pincode)
            if all_medical_stores_name:
                demo = {
                    'medical_stores_list' : all_medical_stores_name,
                }
                return render(request,"display/medical_stores.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_medical_stores_name = medical_storesservice.objects.all()
        demo = {
                    'medical_stores_list' : all_medical_stores_name,
                }
        return render(request,"display/medical_stores.html",demo)

    else:
        all_medical_stores_name = medical_storesservice.objects.all()
        demo2 = {
                'medical_stores_list' : all_medical_stores_name,
        }
    return render(request,"display/medical_stores.html",demo2)
    



def laboratoryfun(request):
    if request.method == "GET":
        pincode = request.GET.get('pincode',"")
        city=request.GET.get('city',"")
        bloodtest= request.GET.get('bloodtest',"off")
        ctscan = request.GET.get('ctscan',"off")
        xray = request.GET.get('xray',"off")
        corona= request.GET.get('corona',"off")
        all_laboratory_name = laboratory.objects.all()
        if pincode:
            all_laboratory_name = all_laboratory_name.filter(laboratory_pincode = pincode)
            if not all_laboratory_name :
                return render(request,"display/pincode_not_found.html") 
        if bloodtest == "on":
            all_laboratory_name = all_laboratory_name.filter(laboratory_bloodtest=1)
        if ctscan == "on":
            all_laboratory_name = all_laboratory_name.filter(laboratory_ctscan=1)
        if xray== "on":
            all_laboratory_name = all_laboratory_name.filter(laboratory_xray=1)
        if corona == "on":
            all_laboratory_name = all_laboratory_name.filter(laboratory_corona=1)
        if bloodtest=="off" and ctscan=="off" and xray=="off" and corona=="off" and pincode=="":
            all_laboratory_name =laboratory.objects.all()
        if city!='':
            all_laboratory_name = all_laboratory_name.filter(laboratory_city__exact = city)
        if not all_laboratory_name:
            return render(request,"display/pincode_not_found.html")
        demo = {
                    'laboratory_list' : all_laboratory_name,
                    'pincode': pincode,
                    'city': city
                }
        return render(request,"display/laboratory.html",demo)
    else:
        all_laboratory_name = laboratory.objects.all()
        demo2 = {
                'laboratory_list' : all_laboratory_name,
        }
    return render(request,"display/laboratory.html",demo2)


def laboratory_description_page(request, laboratory_id):

     laboratory_detail = laboratory.objects.filter(pk=laboratory_id)
     if laboratory_detail:
        demo = {
                    'laboratory_list' : laboratory_detail,
                }
        return render(request,"display/description_page_lab.html",demo)
     else:
          response = "laboratory with id=" + str(id) + " not found."
          return HttpResponse(response)


def laundary(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_laundry_name = laundry.objects.filter(laundry_pincode = pincode)
            if all_laundry_name:
                demo = {
                    'laundry_list' : all_laundry_name,
                }
                return render(request,"display/laundry.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_laundry_name = laundry.objects.all()
        demo = {
                    'laundry_list' : all_laundry_name,
                }
        return render(request,"display/laundry.html",demo)

    else:
        all_laundry_name = laundry.objects.all()
        demo2 = {
                'laundry_list' : all_laundry_name,
        }
    return render(request,"display/laundry.html",demo2)

def lib(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_lib_name = library.objects.filter(library_pincode = pincode)
            if all_lib_name:
                demo = {
                    'library_list' : all_lib_name,
                }
                return render(request,"display/library.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_lib_name = library.objects.all()
        demo = {
                    'library_list' : all_lib_name,
                }
        return render(request,"display/library.html",demo)

    else:
        all_lib_name = library.objects.all()
        demo2 = {
                'library_list' : all_lib_name,
        }
    return render(request,"display/library.html",demo2)


def doctors_description_page(request, doctors_id):

    hostel_detail = docs.objects.filter(pk=doctors_id)
    if hostel_detail:
        demo = {
                    'docs_list' : hostel_detail,
                }
        return render(request,"display/description_page.html",demo)
    else:
	    response = "Hostel with id=" + str(id) + " not found."
	    return HttpResponse(response)

def medical_stores_description_page(request, medical_storesservice_id):

    hostel_detail = medical_storesservice.objects.filter(pk=medical_storesservice_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/medical_stores_desc.html",demo)
    else:
	    response = "Tiffin Service with id=" + str(id) + " not found."
	    return HttpResponse(response)

def library_description_page(request, library_id):

    hostel_detail = library.objects.filter(pk=library_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/lib_desc.html",demo)
    else:
	    response = "Library with id=" + str(id) + " not found."
	    return HttpResponse(response)

def laundry_description_page(request, laundry_id):

    hostel_detail = laundry.objects.filter(pk=laundry_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/laundry_desc.html",demo)
    else:
	    response = "Laundry with id=" + str(id) + " not found."
	    return HttpResponse(response)

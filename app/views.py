from datetime import datetime
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    """Shows the main page"""

    ## Delete customer
    if request.POST:
        if request.POST['action'] == 'delete':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM customers WHERE customerid = %s", [request.POST['id']])

    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers ORDER BY customerid")
        customers = cursor.fetchall()

    result_dict = {'records': customers}

    return render(request,'app/index.html',result_dict)

# Create your views here.
def view(request, id):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers WHERE customerid = %s", [id])
        customer = cursor.fetchone()
    result_dict = {'cust': customer}

    return render(request,'app/view.html',result_dict)

# Create your views here.
def add(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customers WHERE customerid = %s", [request.POST['customerid']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['first_name'], request.POST['last_name'], request.POST['email'],
                           request.POST['dob'] , request.POST['since'], request.POST['customerid'], request.POST['country'] ])
                return redirect('index')    
            else:
                status = 'Customer with ID %s already exists' % (request.POST['customerid'])


    context['status'] = status
 
    return render(request, "app/add.html", context)

# Create your views here.
def edit(request, id):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers WHERE customerid = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE customers SET first_name = %s, last_name = %s, email = %s, dob = %s, since = %s, country = %s WHERE customerid = %s"
                    , [request.POST['first_name'], request.POST['last_name'], request.POST['email'],
                        request.POST['dob'] , request.POST['since'], request.POST['country'], id ])
            status = 'Customer edited successfully!'
            cursor.execute("SELECT * FROM customers WHERE customerid = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
 
    return render(request, "app/edit.html", context)

# Create your views here.
# Bug cannot insert into table
# def login(request):
#     """Shows the login page"""

#     page = 'login'
#     if request.user.is_authenticated:
#         return redirect(index)

#     if request.method == "POST":
#         email = request.POST.get("email").lower()
#         password = request.POST.get("password")

#         try:
#             user = User.objects.get(email=email)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Username OR password does not exit')

#     context = {'page': page}
#     return render(request,'app/login.html', context)

def login(request):
     """Shows the login page"""

     return render(request,'app/login.html')

   # Create your views here.
# def login(request):
#     """Shows the login page"""
#     context = {} 
#     status = ''

#     if request.POST:
#         ## Check if customerid is already in the table
#         with connection.cursor() as cursor:

#             cursor.execute("SELECT * FROM customer WHERE email = %s AND password = %s", [request.POST['email']], [request.POST['email']])
#             customer = cursor.fetchone()
#             ## No customer with same id
#             if customer != None:
#                 ##TODO: age validation
#                 cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s)"
#                         , [request.POST['firstName'], request.POST['lastName'], request.POST['username'],
#                            request.POST['DOB'] , request.POST['psw'], request.POST['psw-repeat'], request.POST['email'] ])
#                 return redirect('index')    
#             else:
#                 status = 'Customer with email %s already exists' % (request.POST['email'])


#     context['status'] = status
#     return render(request,'app/signup.html', context)


    # Create your views here.
def signup(request):
    """Shows the login page"""
    context = {} 
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customer WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            date_time_obj = datetime.fromisoformat(request.POST['DOB'])
            datetime.fromisoformat(request.POST['DOB'])
            if request.POST['psw'] != request.POST['psw-repeat']:
                status = 'Password do not match'
            # elif ((datetime.now().date - date_time_obj).days // 365 < 18):
            #     status = 'Age limt less than 18'
            elif customer == None:
                ##TODO: age validation
                cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['firstName'], request.POST['lastName'], request.POST['username'],
                           request.POST['DOB'] , request.POST['psw'], request.POST['psw-repeat'], request.POST['email'] ])
                return redirect('index')    
            else:
                status = 'Customer with email %s already exists' % (request.POST['email'])


    context['status'] = status
    return render(request,'app/signup.html', context)

def profile(request):
    """Shows the profile page"""

    return render(request,'app/profile.html')








def editpersonalinfo(request):
    """Shows the editpersonalinfo page"""
     context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers WHERE email = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE customers SET first_name = %s, last_name = %s, username = %s, dob = %s, password = %s, confirmPassword = %s, email = %s WHERE email = %s"
                    , [request.POST['first_name'], request.POST['last_name'], request.POST['username'],
                        request.POST['dob'] , request.POST['password'], request.POST['confirmPassword'], request.POST['email'], id ])
            status = 'Customer edited successfully!'
            cursor.execute("SELECT * FROM customers WHERE email = %s", [id])
            obj = cursor.fetchone()

    context["obj"] = obj
    context["status"] = status

    return render(request,'app/editpersonalinfo.html')

def editpersonalcarinfo(request):
    """Shows the editpersonalcarinfo page"""
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listings WHERE owner = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE listings SET car_vin = %s, carmake = %s, model = %s, year = %s, mileage = %s, rate = %s, owner = %s WHERE owner = %s"
                    , [request.POST['car_vin'], request.POST['carmake'], request.POST['model'],
                        request.POST['year'] , request.POST['mileage'], request.POST['rate'], request.POST['owner'], id ])
            status = 'Listing edited successfully!'
            cursor.execute("SELECT * FROM listings WHERE owner = %s", [id])
            obj = cursor.fetchone()

    context["obj"] = obj
    context["status"] = status

    return render(request,'app/editpersonalcarinfo.html')

def editunavailablecarinfo(request):
    """Shows the editpersonalcarinfo page"""
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE unavailable SET car_vin = %s, owner = %s, unavailable = %s WHERE car_vin = %s"
                    , [request.POST['car_vin'], request.POST['owner'], request.POST['unavailable'], id ])
            status = 'Unavailable edited successfully!'
            cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [id])
            obj = cursor.fetchone()

    context["obj"] = obj
    context["status"] = status

    return render(request,'app/editunavailablecarinfo.html')

def editrentalcarinfo(request):
    """Shows the editrentalcarinfo page"""
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM rentals WHERE car_vin = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE rentals SET owner = %s, renter = %s, car_vin = %s, pick_up = %s, drop_off = %s, rental_fee = %s WHERE car_vin = %s"
                    , [request.POST['car_vin'], request.POST['owner'], request.POST['unavailable'], id ])
            status = 'Rental edited successfully!'
            cursor.execute("SELECT * FROM rentals WHERE car_vin = %s", [id])
            obj = cursor.fetchone()

    context["obj"] = obj
    context["status"] = status

    return render(request,'app/editrentalcarinfo.html')

def addpersonalinfo(request):
    """Shows the addpersonalinfo page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customers WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['first_name'], request.POST['last_name'], request.POST['username'],
                           request.POST['dob'] , request.POST['password'], request.POST['confirmPassword'], request.POST['email'] ])
                return redirect('Customers')   #redirects to html file name 
            else:
                status = 'Customer with email %s already exists' % (request.POST['email'])

    context['status'] = status #optional 3rd parameter a dictionary in render() below

    return render(request,'app/addpersonalinfo.html')

def addpersonalcarinfo(request):
    """Shows the addpersonalcarinfo page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM listings WHERE owner = %s", [request.POST['owner']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['car_vin'], request.POST['carmake'], request.POST['model'],
                           request.POST['year'] , request.POST['mileage'], request.POST['rate'], request.POST['owner'] ])
                return redirect('Listings')    #was return redirect('index')
            else:
                status = 'Listing with owner %s and model %s already exists' % (request.POST['owner'],request.POST['model'])

    context['status'] = status

    return render(request,'app/addpersonalcarinfo.html')

def addrentalcarinfo(request):
    """Shows the addrentalcarinfo page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:
            try:
          #      cursor.execute("INSERT INTO rentals VALUES(%s,%s)", [request.POST.get('car_vin'), request.POST.get('pick_up')])
                cursor.execute("INSERT INTO rentals VALUES (%s, %s, %s, %s, %s, %s )"
                        , [request.POST.get('owner'), request.POST.get('renter'), request.POST.get('car_vin'),
                          request.POST.get('pick_up'), request.POST.get('drop_off'), request.POST.get('rental_fee')])
                
            except Exception as e:
                string = str(e)
                message = ""
                if 'duplicate key value violates unique constraint "users_pkey"' in string:  
                    message = 'The email has already been used by another user!'
                elif 'new row for relation "users" violates check constraint "users_email_address_check"' in string:
                    message = 'Please enter a valid email address!'
                elif 'new row for relation "users" violates check constraint "users_mobile_number_check"' in string:
                    message = 'Please enter a valid Singapore number!'
                messages.error(request, message)
                return render(request, "add_Rental.html")
            
    context['status'] = status

    return render(request,'app/addrentalcarinfo.html')

def addunavailablecarinfo(request):
    """Shows the addpersonalcarinfo page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [request.POST['car_vin']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO car_vin VALUES (%s, %s, %s)"
                        , [request.POST['car_vin'], request.POST['owner'], request.POST['unavailable'] ])
                return redirect('Unavailable')    #redirects to HTML file
            else:
                status = 'Unavailablity of owner %s and date %s already exists' % (request.POST['owner'],request.POST['unavailable'])

    context['status'] = status

    return render(request,'app/addunavailablecarinfo.html')

#TO-DO LATER BELOW ALLL 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def Listings(request): # CHANGE NAME TO PERSONAL INFO OR SMTH @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listings ORDER BY owner")
        customers = cursor.fetchall()

    result_dict = {'records': customers}
    
    return render(request,'app/Listings.html',result_dict) #CHANGE TO CORRECT HTML @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def Unavailable(request):
    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM unavailable ORDER BY car_vin")
        customers = cursor.fetchall()

    result_dict = {'records': customers}
    
    return render(request,'app/Unavailable.html',result_dict)

def Rentals(request):
    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM rentals ORDER BY car_vin")
        customers = cursor.fetchall()

    result_dict = {'records': customers}
    
    return render(request,'app/Rentals.html',result_dict)

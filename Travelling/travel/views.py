from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import packagebook, flight, train, bus, hotel, Packages, FlightClass, cab, Airlines, contact, Vehicles, services, flythrough, TarinClass, busClass, hotelproperty, FlightCities, ToFlightCities, FromTrcity, ToTrcity, FromBuscity, ToBuscity, FromCabcity, ToCabcity, CabPrice
hotelproperty
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    service = services.objects.all()
    packages = Packages.objects.filter(adventure=False)
    context = {
        'packages':packages,
        'service' :service
    }
    return render(request,'travels.html', context)


def Login(request):
    if (request.method == 'POST'):
        username = request.POST.get('Username') 
        password = request.POST.get('Password') 

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'messge.html', {'message': "Login Successful",'title': "Continue for booking",'messagetype': "success", "ret":"home"})
        else:
            return render(request, 'messge.html', {'message': "Login Failed",'title': "Please try again? with different credientials",'messagetype': "error", "ret":"login"})
    else:
        return render(request, 'login.html', {'link': 'signin'})


def Book(request):
    if user.is_authenticated:
        return render(request, 'travels.html')
    else:
        return redirect('login')

def Logout(request):
    auth.logout(request)
    return redirect('home')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('email')
        password = request.POST.get('Password')
    
        
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return render(request, 'messge.html', {'message': "Register Successful",'title': "Continue for Login",'messagetype': "success", "ret":"login"})
    return render(request, 'register.html')

@login_required(login_url='login')
def Packagebook(request, pid):
    if request.method == 'POST':
        user = request.user
        packages = Packages.objects.get(id=pid)
        mobNo = request.POST.get('email')
        guestmember = request.POST.get('mobno')
        leaving = request.POST.get('date')

        package = packagebook.objects.create(user=user, package_name=packages, package_mobNo=mobNo, package_leaving=leaving,  package_guestmember=guestmember)
        package.save()
        return render(request, 'messge.html', {'message': "Booked Successful",'title': "More details of your package we will send to your email",'messagetype': "success", "ret":"home"})

def PackageDetail(request, slug):
    package = Packages.objects.get(package_slug=slug)
    vehicle = Vehicles.objects.filter(package=package)
    context = {
        'package':package,
        'vehicle':vehicle,
    }
    return render(request, 'Packagedetails.html', context)
@login_required(login_url='login')
def Flight(request):
    if request.method == 'POST':
        username = request.user
        fromd = request.POST.get('froml')
        tod = request.POST.get('tol')
        todd = get_toamt(tod) 
        ddate = request.POST.get('ddate') 
        adate = request.POST.get('adate') 
        clas = request.POST.get('seat')
        classs = get_cl(clas)
        adult = request.POST.get('adult')
        children = request.POST.get('child')
        trip = request.POST.get('r')
        amount = request.POST.get('amount')
        print(trip)
       

        flights = flight.objects.create(user_name=username, flight_fromd=fromd, flight_tod=todd, flight_ddate=ddate, flight_arival=adate, 
                  flight_classs=classs, flight_adult=adult, flight_Children=children, flight_trip=trip, flight_amount=amount)
        flights.save()
        return render(request, 'messge.html', {'message': "Booked Successfully",'title': "Happy Journey with Explore India",'messagetype': "success", "ret":"home"})
    else:
        fly = flythrough.objects.all()
        flightclass = FlightClass.objects.all()
        city = FlightCities.objects.all()
        tocity = ToFlightCities.objects.all()
        airline = Airlines.objects.all()
        context = {
            'fly':fly,
            'flightclass':flightclass,
            'city':city,
            'tocity':tocity,
            'airln':airline
        }
        return render(request, 'flight.html', context)

def get_cl(am):
    flight = FlightClass.objects.get(flight_price=am)
    return flight.flight_class

def get_toamt(am):
    flight = ToFlightCities.objects.get(price=am)
    return flight.City_name

def Train(request):
    if request.method == 'POST':
        user = request.user
        jfrom = request.POST.get('from')
        jto = request.POST.get('to')
        todd = get_totrainamt(jto) 
        date = request.POST.get('ddate')
        clas = request.POST.get('seat')
        classs = get_tcl(clas)
        amount = request.POST.get('amount')
        adult = request.POST.get('adult')

        trains = train.objects.create(train_jfrom=jfrom, train_jto=todd, train_date=date, user_name=user, train_class=classs, train_amount=amount,
           train_adult=adult)
        trains.save()
        return render(request, 'messge.html', {'message': "Booked Successfully",'title': "Happy Journey with Explore India",'messagetype': "success", "ret":"home"})
    else:
         Train = TarinClass.objects.all()
         Fromtr = FromTrcity.objects.all()
         Totr = ToTrcity.objects.all()
         context = {
             'train':Train,
             'Fromtr':Fromtr,
             'Totr':Totr
             
         }
    return render(request,'train.html', context)


def get_tcl(am):
    trin = TarinClass.objects.get(train_price=am)
    return trin.train_class

def get_totrainamt(am):
    flight = ToTrcity.objects.get(price=am)
    return flight.City_name


def Bus(request):
    if request.method == 'POST':
        bname = request.user
        jfrom = request.POST.get('from')
        jto = request.POST.get('to')
        todd = get_tobusamt(jto) 
        date = request.POST.get('ddate') 
        clas = request.POST.get('seat')
        classs = get_bcl(clas)
        amount = request.POST.get('amount')
        adult = request.POST.get('adult')
        

        buses = bus.objects.create(bus_jfrom=jfrom, bus_jto=todd, bus_date=date, user_name=bname, bus_amount=amount, bus_adult=adult, bus_class=classs)
        buses.save()
        return render(request, 'messge.html', {'message': "Booked Successfully",'title': "Happy Journey with Explore India",'messagetype': "success", "ret":"home"})
    else:
         Bus = busClass.objects.all()
         Frombs = FromBuscity.objects.all()
         Tobs = ToBuscity.objects.all()
         context = {
             'bus':Bus,
             'Frombs':Frombs,
             'Tobs':Tobs
             
         }
    return render(request,'bus.html', context)

def get_bcl(am):
    bs = busClass.objects.get(bus_price=am)
    return bs.bus_class

def get_tobusamt(am):
    flight = ToBuscity.objects.get(price=am)
    return flight.City_name

def Cabs(request):
    if request.method == 'POST':
        cname = request.user
        cfrom = request.POST.get('from')
        cto = request.POST.get('to')
        ddate = request.POST.get('ddate') 
        rdate = request.POST.get('rdate')
        ptime = request.POST.get('ptime')
        carsprice = request.POST.get('CP')

        cabs = cab.objects.create(user_name=cname, cab_from=cfrom, cab_to=cto, cab_departuredate=ddate, cab_returndate=rdate, cab_pickuptime=ptime, Cars_Price=carsprice)
        cabs.save()
        return render(request, 'messge.html', {'message': "Booked Successfully",'title': "Happy Journey with Explore India",'messagetype': "success", "ret":"home"})

    else:
          Fromcb = FromCabcity.objects.all()
          Tocb = ToCabcity.objects.all()
          CrPr = CabPrice.objects.all()
          context = {
              'Fromcb':Fromcb,
              'Tocb':Tocb,
              'CrPr':CrPr
          }
    return render(request, 'cabs.html', context)



@login_required(login_url='login')
def Hotel(request):
    if request.method == 'POST':
        user = request.user
        cityorproprty = request.POST.get('hotelname')
        checkin = request.POST.get('idate')
        checkout = request.POST.get('odate')
        rooms = request.POST.get('rooms')
        adults = request.POST.get('adults')
        childs = request.POST.get('child')
        price = request.POST.get('price')

        hotels = hotel.objects.create(user_name=user, hotel_cityorproprty=cityorproprty, hotel_checkin=checkin, hotel_checkout=checkout,
            hotel_rooms=rooms, hotel_adults=adults, hotel_childs=childs, hotel_price=price )
        hotels.save() 
        return render(request, 'messge.html', {'message': "Hotel Booked Successfully",'title': "Have a nice stay, we sent details on your Email",'messagetype': "success", "ret":"home"})
    else:
         hotl = hotelproperty.objects.all()
         context = {
             'hotl':hotl,
             
         }
    return render(request, 'hotel.html', context)


def Contact(request):
    if request.method == 'POST':
        cname = request.POST.get('fullname')
        print(cname)
        print("*******************************************")
        email = request.POST.get('email')
        description = request.POST.get('msgcontact')

        contacts = contact.objects.create(contact_name=cname, contact_email=email, contact_description=description)
        contacts.save()
    return redirect('home') 

@login_required(login_url='login')
def Bookings(request):
    book = packagebook.objects.filter(user=request.user)
    flights = flight.objects.filter(user_name=request.user)
    trains = train.objects.filter(user_name=request.user)
    buses = bus.objects.filter(user_name=request.user)
    cabs = cab.objects.filter(user_name=request.user)
    hotels = hotel.objects.filter(user_name=request.user)
    context={
        'book':book,
        'Flight':flights,
        'train':trains,
        'Bus':buses,
        'Cab':cabs,
        'Hotel':hotels
    }
    return render(request, 'bookings.html',context)


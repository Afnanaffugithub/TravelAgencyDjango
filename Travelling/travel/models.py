from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.

 


class flight(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    flight_fromd = models.CharField(max_length=50)
    flight_tod = models.CharField(max_length=50)
    flight_ddate = models.DateField()
    flight_arival =  models.CharField(max_length=50, default="No selected")
    flight_classs = models.CharField(max_length=50)
    flight_adult = models.IntegerField()
    flight_Children = models.IntegerField()
    flight_trip = models.CharField(max_length=50)
    flight_amount = models.IntegerField( default=000)

    def __str__(self):
        return self.user_name.username
   

class Packages(models.Model):
    package_name = models.CharField( max_length=50)
    no_of_person = models.IntegerField()
    package_slug = models.SlugField()
    package_price = models.IntegerField()
    package_image = models.ImageField(upload_to='images')
    package_discount = models.CharField(max_length=50)
    package_description = models.TextField(max_length=500)
    adventure =  models.BooleanField(default=False)

    def __str__(self):
        return self.package_name


class train(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    train_jfrom = models.CharField(max_length=50)
    train_jto = models.CharField(max_length=50)
    train_date = models.DateField()
    train_adult = models.IntegerField(default=1)
    train_class = models.CharField(max_length=50)
    train_amount = models.IntegerField( default=000)

    def __str__(self):
        return self.user_name.username


class TarinClass(models.Model):
    train_class = models.CharField(max_length=50)
    train_price = models.IntegerField()

    def __str__(self):
        return self.train_class

class cab(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    cab_from = models.CharField(max_length=50)
    cab_to = models.CharField(max_length=50)
    cab_departuredate = models.DateField()
    cab_returndate = models.DateField()
    cab_pickuptime = models.TimeField()
    Cars_Price = models.CharField(max_length=50, default="SUV")

    def __str__(self):
        return self.user_name.username



class bus(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_jfrom = models.CharField(max_length=50)
    bus_jto = models.CharField(max_length=50)
    bus_date = models.DateField()
    bus_adult = models.IntegerField(default=1)
    bus_class = models.CharField(max_length=50)
    bus_amount = models.IntegerField( default=000)

    def __str__(self):
        return self.user_name.username

class busClass(models.Model):
    bus_class = models.CharField(max_length=50)
    bus_price = models.IntegerField()

    def __str__(self):
        return self.bus_class

class hotel(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_cityorproprty = models.CharField(max_length=50)
    hotel_checkin = models.DateField()
    hotel_checkout = models.DateField()
    hotel_rooms = models.CharField(max_length=50)
    hotel_adults = models.CharField(max_length=50)
    hotel_childs = models.CharField(max_length=50)
    hotel_price = models.CharField(max_length=50)


    def __str__(self):
        return self.hotel_cityorproprty


class Airlines(models.Model):
    airline = models.CharField(max_length=50)

    def __str__(self):
        return self.airline
    
class FlightClass(models.Model):
    flight_class = models.CharField(max_length=50)
    flight_price = models.IntegerField()

    def __str__(self):
        return self.flight_class

class packagebook(models.Model):
    package_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package_name = models.ForeignKey(Packages, on_delete=models.CASCADE)
    package_mobNo = models.CharField(null=False, max_length=10)
    package_guestmember = models.IntegerField(default=1)
    package_leaving = models.DateField()

    def __str__(self):
        return self.user.username

class contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=254)
    contact_description = models.TextField(max_length=500)


    def __str__(self):
        return self.contact_name


    

class Vehicles(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.vehicle_name


class services(models.Model):
    services_number = models.CharField(max_length=50)
    services_title = models.CharField(max_length=50)
    services_description = models.TextField(max_length=500)

    def __str__(self):
        return self.services_title



class flythrough(models.Model):
    fly_image = models.ImageField(upload_to='images')
    fly_title = models.CharField(max_length=50)
    fly_description = models.TextField(max_length=500)

    def __str__(self):
        return self.fly_title

class FlightCities(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return self.City_name

class ToFlightCities(models.Model):
    City_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.City_name


class hotelproperty(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return self.City_name

class FromTrcity(models.Model):
    City_name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.City_name

class ToTrcity(models.Model):
    City_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.City_name

class FromBuscity(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return self.City_name

class ToBuscity(models.Model):
    City_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.City_name


class FromCabcity(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return self.City_name

class ToCabcity(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return self.City_name

class CabPrice(models.Model):
    Car_Price = models.CharField(max_length=50)

    def __str__(self):
        return self.Car_Price


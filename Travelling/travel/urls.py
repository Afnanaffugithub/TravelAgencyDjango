from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('register/',views.Register, name="register"),
    path('packagebook/<int:pid>/',views.Packagebook, name="packagebook"),
    path('flight/', views.Flight, name="flight"),
    path('train/', views.Train, name="train"),
    path('bus/', views.Bus, name="bus"),
    path('hotel/', views.Hotel, name="hotel"),
    path('cab/', views.Cabs, name="cab"),
    path('contact/', views.Contact, name="contact"),
    path('packagedetail/<str:slug>/', views.PackageDetail, name='packagedetail'),
    path('bookings/', views.Bookings, name='bookings'),
]
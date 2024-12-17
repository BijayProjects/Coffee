from django.urls import path
from .import views


urlpatterns =[
    path('', views.Home.home, name='home'),
    path('about/',views.About.about,name='about'),
    path('contact/',views.Contact.contact,name='contact'),
    path('Menu/',views.Menu.menu, name='menu'),
    path('Reservation/',views.Reservation.reservation,name='reservation'),
    path('Service',views.Service.service,name='service'),
    path('Testimonial/',views.Testimonial.testimonial,name='testimonial'),
]
from django.shortcuts import render,redirect
from BCH_Admin.models import our_story,our_vision
from BCH_Admin.models import HotCoffee,ColdCoffee,Offer_Service,Offer_Email,Table_Booking
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.

class Home():
    def home(request):
        if request.method == 'POST':
            reg_email = request.POST['reg-email']

            register_email = Offer_Email(offer_email = reg_email)
            register_email.save()

        hotCoffee =HotCoffee.objects.all()
        paginator = Paginator(hotCoffee, 4)
        page_number = request.GET.get('page?')
        hot_coffee = paginator.get_page(page_number)

        coldCoffee = ColdCoffee.objects.all()
        paginator_cold = Paginator(coldCoffee, 4)
        page_counter = request.GET.get('page?')
        cold_coffee = paginator_cold.get_page(page_counter)

        offer_service= Offer_Service.objects.all()


        vision = our_vision.objects.all()
        story = our_story.objects.all

        context = {
            'vision': vision,
            'story':story,
            'hotCoffee':hot_coffee,
            'coldCoffee':cold_coffee,
            'offer_service':offer_service
        }

        return render(request, 'main/index.html',context)
    
class About():

    def about(request):
        return render(request, 'main/about.html')
    
class Contact():
    def contact(request):
        return render(request, 'main/contact.html')

class Menu():
    def menu(request):
        products =HotCoffee.objects.all()
        products1 = ColdCoffee.objects.all()
          
        return render(request, 'main/menu.html',{'products':products,'products1':products1})
    
class Reservation():
    def reservation(request):
        if request.method =='POST':
            username = request.POST['username']
            email = request.POST['email']
            date = request.POST['date']
            time = request.POST['time']
            number_of_person = request.POST['number_of_person']
            reversed_table = Table_Booking(name=username, email=email,date=date,time=time,person=number_of_person)
            reversed_table.save() 
            return HttpResponse('One Full Table is Booked for You.')                            

        return render(request, 'main/reservation.html')
    
class Service():
    def service(request):
        return render(request, 'main/service.html')

class Testimonial():
    def testimonial(request):
        return render( request, 'main/testimonial.html')
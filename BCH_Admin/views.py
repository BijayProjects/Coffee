from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import our_story,our_vision,HotCoffee,ColdCoffee,Offer_Service,Table_Booking
import os

# Create your views here.
class AuthenticationAdmin():
    def admin_login(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            admin_user = User.objects.filter(username = username)

            if not admin_user.exists():
                messages.info(request, f'{username} Username id not recorded as admin manager ** ') 
                return redirect('admin-login')   
            
            admin_user = authenticate(username=username, password= password)

            if admin_user is not None and admin_user.is_superuser:
                login(request, admin_user)
                return redirect('dashboard')
            messages.info(request, 'Invalid password')
            return redirect('admin-login')    
        return render(request, 'main/login.html')
    
    @login_required(login_url='admin-login')
    def SignOut(request):
        logout(request)
        messages.info(request, 'LogOut Successfully')
        return redirect('admin-login')

class Dashboard():
    @login_required(login_url='admin-login')
    def dashboard(request):
        
        return render(request, 'main/dashboard.html')


class AdminPages():
    @login_required(login_url='admin-login')
    def myprofile(request):
        return render(request, 'main/myprofile.html')
    
    @login_required(login_url='admin-login')
    def Error_404(request):
        return render(request, 'main/404.html')
    
    def blank(request):
        return render(request, 'main/blank.html')
    
    def admin_menu(request):
        return render(request, 'main/admin_menu.html')
    
    def abouts(request):


        about_show_story= our_story.objects.all()
        about_show_vision= our_vision.objects.all()


        context= {
            "about_show_story":about_show_story,
            "about_show_vision":about_show_vision
            
        }
        return render(request, 'main/abouts.html',context)
    
    def forgot_password(request):
        return render(request, 'main/forgot-password.html')
    
    def table(request):
        if request.method =='POST':
            Name = request.POST['name']
            Number_of_person =request.POST['number-of-person']
            Email = request.POST['email']
            Date = request.POST['date']
            Time = request.POST['time']
            Check_table = request.POST['check_booking']
            add_Booking = Table_Booking(name = Name, email=Email, date=Date, time = Time, person = Number_of_person, check_table=Check_table)
            add_Booking.save()
            messages.success(request, 'Booking Successfully Requested')
            return redirect('table')


        
        book_info = Table_Booking.objects.all()

        context = {
            'book_info':book_info
        }
        return render(request, 'main/booking_table.html',context)
    
    def service(request):
        return render(request, 'main/admin_service.html')
    
    def offer_services(request):
        try:
            if request.method== 'POST':
                discount = request.POST['discount']
                des = request.POST['descriptions']
                event_time = request.POST['event-time']

                reg_serv = Offer_Service(discount_percent = discount, descriptions = des, offer_starting_time = event_time)
                
                reg_serv.save()
                messages.success(request, 'Offer Service added Successfully..')
                return redirect('offer_services')   
            
        except:      
            messages.info(request,  'Please enter the word')  
            return redirect('offer_services')
        
        show_offer = Offer_Service.objects.all()
        return render(request, 'main/offer_services.html',{'show_offer':show_offer})

    def cold_coffee(request):

        view_cold_coffee = ColdCoffee.objects.all()
        return render(request, 'main/coldcoffee.html',{'view_cold_coffee':view_cold_coffee})
    
    def hot_coffee(request):
        view_product = HotCoffee.objects.all()
        return render(request, 'main/hotcoffee.html',{'viewProduct':view_product})

def offer_update(request,id):
    if request.method == 'POST':
        upOffer = Offer_Service.objects.get(id=id)

        upOffer.discount_percent = request.POST['discount']
        upOffer.descriptions = request.POST['descriptions']
        upOffer.offer_starting_time = request.POST['event-time']

        upOffer.save()
        messages.success(request, 'Offer Service Updated Successfully..')
        return redirect('offer_services')
    upOffer = Offer_Service.objects.get(id=id)
    return render( request, 'main/update_offer.html',{'upOffers':upOffer})
    

       
class Update():
    
    def vision_update(request, id):
        if request.method == 'POST':
            vu = our_vision.objects.get(id=id)
            vu.sub_body = request.POST['new_vision_update']
            vu.save()
            messages.success(request, 'Successfully Updated Vision of BCH')
            return redirect('abouts')

        vu = our_vision.objects.get(id=id)
        context = {
            'vu':vu
        }
        return render(request, 'main/visionUpdate.html',context)
    
    def story_update(request, id):
        if request.method == 'POST':
            su = our_story.objects.get(id=id)
            su.sub_body = request.POST['new_story_update1']
            su.main_body = request.POST['new_story_update2']
            su.save()
            messages.success(request, 'Successfully Updated Story of BCH')
            return redirect('abouts')

        su = our_story.objects.get(id=id)
        context = {
            'su':su
        }
        return render(request, 'main/storyUpdate.html',context)
    

class Add_Coffee():
    def add_hot_coffee(request):
        if request.method == 'POST' and request.FILES:
            title = request.POST['title']
            descriptions = request.POST['descriptions']
            price = request.POST['price']
            image = request.FILES['image']
            items = HotCoffee(title=title,descriptions=descriptions,price=price,images=image)
            items.save()
            return redirect('hotcoffee')
        
        return render(request, 'hotcoffee/addcoffee.html')
    
    def add_cold_coffee(request):
        if request.method == 'POST' and request.FILES:
            title = request.POST['title']
            descriptions = request.POST['descriptions']
            price = request.POST['price']
            img = request.FILES['image']
            items1 = ColdCoffee(title=title,descriptions=descriptions,price=price,images=img)
            items1.save()
            return redirect('coldcoffee')

        return render(request, 'coldcoffee/addcoffee.html')

def hot_items_delete(request,id):
    prod = HotCoffee.objects.get(id=id)
    if len(prod.images)>0:
        os.remove(prod.images.path)
    prod.delete()
    messages.success(request, 'Successfully Remove the Product')
    return redirect('hotcoffee')

def cold_items_delete(request,id):
    prod = ColdCoffee.objects.get(id=id)
    if len(prod.images)>0:
        os.remove(prod.images.path)
    prod.delete()
    messages.success(request, 'Successfully Remove the Product')
    return redirect('coldcoffee')

class Delete_item():
    def offer(request,id):
        off = Offer_Service.objects.get(id=id)
        off.delete()
        messages.success(request, 'Service Deleted successfully')
        return redirect('offer_services')

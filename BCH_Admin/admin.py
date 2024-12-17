from django.contrib import admin
from .models import our_story,our_vision,Table_Booking
# Register your models here.

admin.site.register(our_story)
admin.site.register(our_vision)

@admin.register(Table_Booking)
class Table_BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','date','time','person','check_table']
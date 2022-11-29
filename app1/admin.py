from django.contrib import admin
from app1.models import Bookappoinment,Bookappoinmenttime
# Register your models here.

class BookappoinmentAdmin(admin.ModelAdmin):
	list_display=['Patient_Name','PhoneNumber','Patient_Cause','Patient_Doctor','Patient_City']

admin.site.register(Bookappoinment,BookappoinmentAdmin)

admin.site.register(Bookappoinmenttime)

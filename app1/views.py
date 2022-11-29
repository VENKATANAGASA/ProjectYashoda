from django.shortcuts import render,redirect
from app1.forms import Bookappoinmentform,Bookappoinmentdateform
from django.contrib.auth.decorators import login_required
from app1.models import Bookappoinment,Bookappoinmenttime

# Create your views here.

def home(request):
	return render(request,'app1/home.html')

def about(request):
	return render(request,'app1/about.html')


def gallery(request):
	return render(request,'app1/gallery.html')

def services(request):
	return render(request,'app1/services.html')
	
def deparments(request):
	return render(request,'app1/deparments.html')

def bookappoinment(request):
	return render(request,'app1/bookappoinment.html')

def findyourdoctor(request):
	form=Bookappoinmentform()
	if request.method=="POST":
		form=Bookappoinmentform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bookappoinment')
	return render(request,'app1/findyourdoctor.html',{'f':form})

def calendar(request):
	form=Bookappoinmentdateform()
	if request.method=="POST":
		form=Bookappoinmentdateform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bookappoinment')
	return render(request,'app1/calendar.html',{'f':form})

def detailsview(request):
	form=Bookappoinmentdetailsform()
	if request.method=="POST":
		form=Bookappoinmentdetailsform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bookappoinment')
	return render(request,'app1/detailsview.html',{'f':form})

@login_required
def onlinevideoconsulation(request):
	a=Bookappoinment.objects.all()
	b=Bookappoinmenttime.objects.all()
	return render(request,'app1/onlinevideoconsulation.html',{'a':a,'b':b})

def logout(required):
	return render(request,'app1/logout.html')
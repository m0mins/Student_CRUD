from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from studentProfileApp import models
from django.shortcuts import redirect
from studentProfileApp.forms import ProfileForm
from studentProfileApp.models import Profile
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='GET':
        search=request.GET.get('src')
        if search:
            prof=Profile.objects.filter(name__icontains=search)
            if not prof:
                messages.warning(request, "Your account is about to expire.") 

        else:
            prof=Profile.objects.all()
            
    context = {'prof':prof}
    return render(request,'studentProfileApp/home.html',context)

def signUP(request):
    form=ProfileForm()
    registration=False
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            registration=True
            return HttpResponseRedirect(reverse('studentProfileApp:home'))
    dict={'form':form,'registration':registration}
    return render(request,'studentProfileApp/signUp.html',context=dict)

def studentDetails(request, pk):
    student_id = Profile.objects.get(id=pk)
    context = {'student_id':student_id}
    return render(request, 'studentProfileApp/studentDetails.html', context)

def editStudent(request, pk):
    student_id = Profile.objects.get(id=pk)
    form = ProfileForm(instance=student_id )
    
    if request.method == "POST":
        form=ProfileForm(request.POST,request.FILES, instance=student_id)
        if form.is_valid():
            form.save()
            form=ProfileForm(instance=student_id)
            return HttpResponseRedirect(reverse('studentProfileApp:home'))
    context = {'form':form}
    return render(request, 'studentProfileApp/signUp.html', context)

def studentDelete(request, pk):
    student_data = Profile.objects.get(id=pk)
    student_data.delete()
    return HttpResponseRedirect(reverse('studentProfileApp:home'))


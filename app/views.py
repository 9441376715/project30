from django.shortcuts import render
from app.froms import *
from django.http import HttpResponse 
# Create your views here.


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            PW=ufd.cleaned_data['password']
            MUFDO.set_password(PW)
            MUFDO.save()
            MPFDO=pfd.save(commit=False)
            
            MPFDO=Username=MUFDO
            MPFDO.save()
            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('Invalid data')
                               

    return render(request,'registration.html',d)
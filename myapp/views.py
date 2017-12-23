from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .models import Client
from main import settings
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required







@login_required
def clients(request):
    curr=request.user
    return render_to_response('clients.html',{'user':curr,'clients':Client.objects.filter(userid=curr.id)})

@csrf_protect
def auth_view(request):
    if request.method == 'POST':
     username = request.POST.get('username','')
     password = request.POST.get('password','')
     user = authenticate(username=username,password=password)

     if user is not None:
      if user.is_active:
       login(request, user)
       next = request.GET.get('next','/home/')
       return HttpResponseRedirect(next)
      else:
       HttpResponse("Inactive User")
     else:
      return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request,'login.html',{'redirect_to':next})



@login_required
def home(request):
    curr=request.user
    if curr.is_staff:
     return render(request,'home.html',{'user':request.user})
     #return render(request,'clients.html',{'clients':Client.objects.filter(userid=curr.id)})
    else:
     return render(request,'dummy.html',{'clients':Client.objects.filter(clientname=curr.clientid)})

def invalid_login(request):
    return render_to_response('invalid_login.html')

@login_required
def getout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

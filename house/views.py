
from django.shortcuts import render, redirect
from .forms import RegisterForm,SigninForm

# Create your views here.

def house(response):
    if response.method =="POST":
          form = RegisterForm(response.POST)
          if form.is_valid():
              form.save()
              username = form.cleaned_data.get('username')
              raw_password = form.cleaned_data.get('password1')
              user = authenticate(username=username, password=raw_password)
              login(response, user)
          return redirect("/home")    
    else:         
        form = RegisterForm()

    return render(response,"house/house.html",{"form":form})

def home(request):
  return render(request, 'house/home.html')   

def services(request):
  return render(request, 'house/services.html')    

def register(request):
    if request.method == 'POST':
          form = SigninForm(request.POST)
          if form.is_valid():
                return HttpResponseRedirect('/home/')
    else:  
      form = SigninForm()          
    return render(request, 'house/register.html',{'form':form})    
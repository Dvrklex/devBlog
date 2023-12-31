from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.

class ViewRegistro(View):
    
    def get(self,request):
        context = {"sign_up":"user/css/sign_up.css"}
        form = CustomUserCreationForm()  # Utiliza el formulario personalizado
        return render(request,'user/sign_up.html',{"form":form,"context":context})
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)  # Utiliza el formulario personalizado
        
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            
            return redirect('Home')
        else: 
            context = {"register":"user/css/sign_up.css"}
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,'user/sign_up.html',{"form":form,"context":context})
      



def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

     
def login_view(request):
    view_name= 'Login'
    context = {'css_file':"user/css/login.css"}
    form = AuthenticationForm(request,data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request,"Usuario inválido")
        else:
            messages.error(request,"Información incorrecta")
    return render(request,'user/login.html',{"view_name":view_name,"context":context,"form":form})


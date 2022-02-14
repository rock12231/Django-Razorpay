from urllib.request import Request
from django.views import View

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


class Home(View):
    def get(self, request):
        return render(request, 'pay/app.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password,"username........, password.......")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login Successful")
            return render(request, 'pay/app.html',{'user':user})
        else:
            print("Login Failed")
        return render(request, 'pay/app.html')

def Logout(request):
    logout(request)
    return redirect('home')
    
    
    
    
def gitRepo():
    username = input("Enter the github username:")
    request = Request.get('https://api.github.com/users/'+username+'/repos')
    json = request.json()
    for i in range(0,len(json)):
        print("Project Number:",i+1)
        print("Project Name:",json[i]['name'])
        print("Project URL:",json[i]['svn_url'],"\n")
        
        

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

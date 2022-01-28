from urllib.request import Request
from django.shortcuts import render
from django.views import View

# Create your views here.

# def index(request):
#     return render(request, "pay/app.html")


class Home(View):
    def get(self, request):
        return render(request, 'pay/app.html')

    def post(self, request):
        email = request.POST.get('email')
        return render(request, 'pay/app.html')
    
def gitRepo():
    username = input("Enter the github username:")
    request = Request.get('https://api.github.com/users/'+username+'/repos')
    json = request.json()
    for i in range(0,len(json)):
        print("Project Number:",i+1)
        print("Project Name:",json[i]['name'])
        print("Project URL:",json[i]['svn_url'],"\n")
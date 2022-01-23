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

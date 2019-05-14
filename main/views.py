from django.shortcuts import render
from django.shortcuts import redirect

from .forms import frm_login
# Create your views here.
#from django.http import HttpResponse

def login(request):
    
    if request.method == 'POST':
        print('++++> Post <++++')
        form = frm_login(request.POST)
        if form.is_valid():
            
            return redirect('home')
    else:
        form = frm_login()
    return render(request,'login/index.html',{'frm':form})


def home(request):
    return render(request,'user/home.html')
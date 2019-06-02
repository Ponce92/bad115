from django.contrib.auth                import login,authenticate
from django.shortcuts                   import render
from django.shortcuts                   import redirect
from django.contrib.auth.decorators     import login_required
from main.models                        import Users



#--------------------------------------------------------------------------------------------------
@login_required
def home(request):
    user=request.user
    return render(request,'user/home.html',{'user':user})
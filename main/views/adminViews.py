from django.shortcuts                   import render
from django.shortcuts                   import redirect
from django.http                        import JsonResponse
from django.template.loader             import render_to_string
from django.contrib.auth.decorators     import login_required

from main.models            import Roles
from django.db              import connection
from main.forms             import CrtRolForm

@login_required
def roles(request):
    user=request.user
    roles=Roles.objects.exclude(rol_code='ADIT')
    crtFrm = CrtRolForm()

    return render(request,'admin/roles.html',{'user':user,'roles':roles,'crtForm':crtFrm})

def create_rol(request):
    if request.method == 'POST':
        form =CrtRolForm(request.POST)
        if form.is_valid():
            data['data_state']=True
        else:
            data['data_state']=False
    else:
        form=CrtRolForm()

    context={
        'crtForm' : form
        }
    html=render_to_string('admin/crtRolFrg.html',context,request=request)
    return JsonResponse({'html_form':html})
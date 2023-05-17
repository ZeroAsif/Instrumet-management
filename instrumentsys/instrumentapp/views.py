from django. contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import AddInsrument,BookInstrument

# Create your views here. 

@login_required(login_url= 'login')
def HomePage(request):
    data = AddInsrument.objects.all()
    return render (request,'home.html',{'data':data,})

def SignupPage(request):
    if request.method=='POST':  
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(username=username,password=pass1)
        if user is not None and user.is_staff==False:
            login(request,user)
            return redirect('home')
        elif user is not None and user.is_staff==True:
            login(request,user)
            return redirect("admins")
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


# LogOut Here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
def LogoutPage(request):
    logout(request)
    return redirect('login')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Adminpage(request):
    obj = AddInsrument.objects.all()
    return render(request, "admin.html",{'obj':obj})

def Addinstrument(request):
    try:
        if request.method == 'POST':
            I_name = request.POST.get('in','')
            i_desc = request.POST.get('idesc','')
            i_img = request.FILES['img']
            obj = AddInsrument(instrument_name = I_name,instrument_desc = i_desc, instrument_img = i_img )
            obj.save()
            messages.success(request,"Add Insruments Successfully")
            return redirect('admins')
    except:
        messages.error(request,"Please Fill Correct Information")
        return redirect('admins')
    

def Bookinstrument(request):
    user = request.user.id
    id = User.objects.get(id=user)
    try:
        if request.method == 'POST':
            name = request.POST.get('name', '')
            iname = request.POST.get('iname','')
            email = request.POST.get('email', '')
            date = request.POST.get('date', '')
            st = request.POST.get('st', '')
            et = request.POST.get('et', '')
            obj = BookInstrument(user= id,your_name= name,iname=iname,email = email,date = date,st = st,et = et)
            obj.save()
            messages.success(request,'Instrument Book Successfully')
            return redirect('home')
    except:
        messages.error(request,"Somethig Went Wrong!")
        return redirect('home')
    
def Approvel(request):
    # get count
    Aprove_count = BookInstrument.objects.all().count()
    print('*****************',Aprove_count)

    obj = BookInstrument.objects.all()
    if request.method == 'POST':
        id_list = request.POST.getlist('boxes')
        
        # update database
        for x in id_list:
            BookInstrument.objects.filter(pk=int(x)).update(Aprove = True)
        messages.success(request,"Approval Successfull")
        return redirect('admins') 
    return render(request,"approvel.html",{'obj':obj, 'Aprove_count':Aprove_count})

def Status(request): 
    user = request.user.id
    user_id = User.objects.get(id=user)
    data = BookInstrument.objects.filter(user_id=user_id)
    return render(request, "status.html",{'data':data})


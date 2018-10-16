from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Core,Rest,Menu,Order
from .form import LoginForm,OrderForm
from django.contrib.auth import authenticate


def login(request):
    #message="alert('you successfully login')"
    if request.method=='POST':
        myloginform=LoginForm(request.POST)
        if myloginform.is_valid():
            usern = myloginform.cleaned_data.get("username")
            passw = myloginform.cleaned_data.get("password")



            user = authenticate(username=usern, password=passw)
            if user is not None:
                request.session['username'] = usern
                nu=len(Order.objects.filter(user_name=user))
                request.session['ordernumber']=nu
                try:
                    oid=request.session["orderid"]
                except:

                    return redirect("/home/")
                else:
                    del request.session["orderid"]

                    return redirect("/home/rpage/order/"+str(oid))
    else:
        myloginform=LoginForm()
    return render(request,"myapp/login.html",{"form":myloginform})

def home(request):
    a=Core.objects.all()
    try:
        user=request.session["username"]
        num=request.session["ordernumber"]
    except:
        return render(request,"myapp/home.html",{"location":a})
    else:
        return render(request, "myapp/home.html", {"location": a,'user':user,'number':num})


def resturant(request,rid):
    a=Core.objects.get(id=rid)
    try:
        user = request.session["username"]
        num = request.session["ordernumber"]
    except:
        return render(request, "myapp/rest.html", {'Restu': a})
    else:
        return render(request, "myapp/rest.html", {'Restu': a, 'user': user, 'number': num})



def rmenu(request,mid):
    x=Rest.objects.get(id=mid)
    try:
        user = request.session["username"]
        num = request.session["ordernumber"]
    except:
        return render(request, "myapp/menupage.html", {'menusample': x})
    else:
        return render(request, "myapp/menupage.html", {'menusample': x, 'user': user, 'number': num})



def orderpage(request,oid):
    request.session["orderid"]=oid
    doneorder=False
    num=0
    user=''
    try:
        user=request.session["username"]
        num = request.session["ordernumber"]
    except:
        return redirect("/login/")
    else:
        m=Menu.objects.get(id=oid)
        if request.method=='POST':
            myform=OrderForm(request.POST)
            if myform.is_valid():
                oqty=myform.cleaned_data.get("qty")
                opay=m.mprice*oqty
                query=Order.objects.create(o_id=m,o_qt=oqty
                                     ,pay=opay,
                                     d_time=datetime.now(),
                                     user_name=user)
                query.save()
                doneorder=True

        else:
            myform=OrderForm()
        return render(request,"myapp/orderpage.html",
                      {"menu":m,"form":myform,"status":doneorder,'user':user,'number':num})

def cart(request):
    request.session["cartpage"]=True
    try:
       user = request.session["username"]
    except:
        return redirect("/login/")
    else:
        orders = Order.objects.filter(user_name=user)
        payment=sum(x.pay for x in orders)
        payment=payment+payment*0.18
        return render(request,"myapp/cart.html",{"orders":orders,"pay":payment})

def payment (request):
    add=request.POST.get("address1",False)
    add2=request.POST.get("address2",False)
    pay=request.POST.get("pay",False)
    if add!=False and add2!=False :
        if pay=='card':
            "payment gateway"
        if pay=='cod':
            return render(request,"myapp/cod.html",{"add":add+','+add2})
    else:
        pass
    return render(request,"myapp/pay.html")

def cartdelete(request,cid):
   Order.objects.filter(id=cid).delete()
   return redirect("myapp:cartpage")

def paymentgateway (request):
    return HttpResponse("<h>on payment page</h>")

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            susername=form.cleaned_data.get('username')
            spassword=form.cleaned_data.get("password1")
            user=authenticate(username=susername,password=spassword)
            return redirect("/login/")
    else:
        form=UserCreationForm()
    return render(request,"myapp/signup.html",{"form":form})

def logout(request):
    del request.session["username"]
    return redirect("/login/")

def first(request):
    return render(request,"myapp/default.html")
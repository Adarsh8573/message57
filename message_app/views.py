from django.shortcuts import render,HttpResponse,redirect
from .models import Msg
# Create your views here.

def demo(request):
    return HttpResponse("Hello !! working property")

def create(request):
   # print("Request is:",request.method)
    if request.method=='POST':
        #fatch values from the form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
       # print("Name:",n)
       # print("Email:",mail)
       # print("mobile:",mob)
       # print("Message:",msg)
        return redirect('/')
       # return HttpResponse("Data fetched  successfully")
    else:
        return render(request,'create.html')



def dashboard(request):
   m=Msg.objects.all()
  # print(m)
   context={}
   context['data']=m
   return render(request,'Dashboard.html',context)
  # return HttpResponse("Data fetched from database !!")

def delete(request,rid):
    #print("Id to be delete:",rid)
    m=Msg.objects.get(id=rid)
    print(m)
    m.delete()
    return redirect('/')
    #return HttpResponse("Id to be deleted:"+rid)

def edit(request,rid):
   # print("Id to be edited:")
   if request.method=='POST':
    #udate data
     n=request.POST['uname']
     mail=request.POST['uemail']
     mob=request.POST['mobile']
     msg=request.POST['msg']
     print(n,"-",mail,"-",msg)
     return render("/")
   else:
    #display form with previous fileds
    m=Msg.objects.get(id==rid)
    print(m)
    context={}
    context['data']=m
    return render(request,'edit.html',context)
    #return HttpResponse("Id to be edited"+rid)
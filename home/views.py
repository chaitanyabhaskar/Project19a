from email import message
import imp
from xml.dom.minidom import Document
from home.models import ChangesDetails, ExamDetails, staff
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib import messages
from res.models import Slots
from django.core.paginator import Paginator

# Create your views here.
global lst
def adm(request):
    return render(request,'homeadmin.html')
def adm1(request):
    eid=request.POST['Examid']
    d=ExamDetails.objects.raw('SELECT dt From home_examdetails where id='+str(eid))
    print(d)
    return render(request,'homeadmin.html',{'date':1})
def usr1(request):
    lst=[]
    usr=request.user.username
    try:
        o=staff.objects.get(id=usr)
    except:
        return render(request,'home.html')
    for i in ExamDetails.objects.raw('SELECT * from home_examdetails'):
        lst.append(i.id)
    if request.method=='POST':
        ol=[]
        eid=request.POST['Examid']
        d=ExamDetails.objects.get(id=str(eid))
        for i in Slots.objects.raw('select * from res_slots where fid_id=\''+str(usr)+'\''+' and "Eid_id"=\''+str(eid)+'\' order by date asc'):
            ol.append(i)
        return render(request,'home.html',{'lst':lst,'date':d.dt,'eid':eid,'usr':o.name,'obj':ol})
    return render(request,'home.html',{'lst':lst,'usr':o.name})
def adm2(request):
    if request.method=='POST':
        days=request.POST['days']
        if days == '':
            messages.info(request,'Field 1 cant be empty')
            return redirect(adm)
        eid=request.POST['Eid']
        date=request.POST['date']
        if ExamDetails.objects.filter(id=eid).exists():
            messages.info(request,'Examid Already exists, Please use another ID')
            return redirect('adm')
        lst=[i for i in range(1,int(days)+1)]
        return render(request,"homeadmin2.html",{'lst':lst,'le':len(lst),'eid':eid,'dt':date})
    return render(request,'homeadmin2.html',{'lst':lst,'le':len(lst),'eid':eid,'dt':date})
    
def adm3(request):
    lst=[]
    for i in ExamDetails.objects.raw('SELECT * from home_examdetails'):
        lst.append(i.id)
    if request.method=='POST':
        ol=[]
        lo=[]
        eid=request.POST['Examid']
        d=ExamDetails.objects.get(id=str(eid))
       
        for i in Slots.objects.raw('select * from res_slots where "Eid_id"=\''+str(eid)+'\' order by date asc'):
            ol.append(i)
            
        return render(request,'homeadmin3.html',{'lst':lst,'date':d.dt,'eid':eid,'obj':ol})
    return render(request,'homeadmin3.html',{'lst':lst})
def adm4(request):
    if request.method=='POST':
        id=request.POST['ID']
        dt=request.POST['Dt']
        l=[]
        for i in Slots.objects.raw("select * from res_slots where fid_id='"+id+"' and date='"+dt+"'"):
            l.append(i)
            v=i.fid_id
            return render(request,'homeadmin4.html',{'obj':l,'fid_id':v})
    return render(request,'homeadmin4.html')
def adm6(request):
    fid=request.POST['cid']
    date=request.POST['dot']
    id=request.POST['did']
    db=ChangesDetails(Date=date,Id=fid,RId=id)
    db.save()
    print(fid,id,date)
    for i in Slots.objects.raw("select * from res_slots where fid_id='"+str(fid)+"' and date='"+str(date)+"'"):
            i.fid_id=id
            i.save()
    return render(request,'result2.html')
def adm7(request):
    return render(request,'usr2.html')
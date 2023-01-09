import math
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
import pandas as pd
import random
from math import ceil
from home.models import ExamDetails, staff
from res.models import Slots
def res(request):
    data=pd.read_excel("C:\\Users\\chala\\OneDrive\\Documents\\facultylist.xlsx")
    data1=pd.read_excel("C:\\Users\\chala\\OneDrive\\Documents\\slotslist.xlsx")
    l0=list(data1["Slot-Value"])
    l1=list(data1["Dep-RNo"])
    l2=list(data["Faculty_id"])
    fl=list(l2)
    f={}
    le=request.POST['Days']
    eid=request.POST['eid']
    dt=request.POST['dt']
    lt=[i for i in range(1,int(request.POST['Days'])+1)]
    lst=[]
    for i in range(1,int(request.POST['Days'])+1):
        v1=request.POST['session1Day'+str(i)]
        v2=request.POST['session2Day'+str(i)]
        n=0
        if v1=='' and v2=='':
            messages.info(request,'Any Both sessions cant be empty on a single day')
            return render(request,'homeadmin2.html',{'lst':lt,'le':le,'dt':dt})
        if request.POST['session1Day'+str(i)]=='':
            v1=0
        if request.POST['session2Day'+str(i)]=='':
            v2=0
        lst.extend([math.ceil(int(v1)/30.0),math.ceil(int(v2)/30.0)])
    limit=math.ceil(sum(lst)/len(l2))
    print(limit)
    sw=1
    def Alott(l0,l1,li,n):
        d={}
        i=0
        index=0
        while(i<n):
            for k in range(l0[index]):
                if l1[index] in d.keys():
                    d[l1[index]]=d[l1[index]]+','+ str(li[i])
                else:
                    d[l1[index]]=str(li[i])
                i+=1
                if i==n:
                    break
            index+=1
        return d
    l=[]
    for i in lst:
        if sw==0:
            for k,v in f.items():
                if v>=limit:
                    l2=list(set(l2)-set([k]))
        else:
            sw=0
        random.shuffle(l2)
        li=l2[:i]
        if sum(l0)>=i and len(fl)>=i:
            l.append(Alott(l0,l1,li,i))
        else:
            return render(request,'failed.html',{'l':i})
    ind=1
    c=1
    print(l)
    db0=ExamDetails(id=eid,dt=dt)
    db0.save()
    for i in l:
        cls=list(i.keys())
        ids=list(i.values())
        
        for j in range(len(cls)):
            if ids[j]=='':
                continue
            if ids[j].find(',')!=-1:
                s=ids[j].split(',')
                for k in s:
                    db=Slots(sno=c,fid=staff.objects.get(id=k),Eid=ExamDetails.objects.get(id=request.POST['eid']),rno=cls[j],date=request.POST['day'+str(ind)])
                    db.save()
            else:
                db=Slots(sno=c,fid=staff.objects.get(id=ids[j]),Eid=ExamDetails.objects.get(id=request.POST['eid']),rno=cls[j],date=request.POST['day'+str(ind)])
            db.save()
        df=pd.DataFrame(list(zip(cls,ids)),columns=['class','Id'])
        df.to_excel ('C:\\Users\\chala\\OneDrive\\Desktop\\Project_OutPut\\'+str('day'+str(ind))+'session'+str(c)+'.xlsx', index = False, header=True)
        c+=1
        if c<=2:
            continue
        else:
            c=1
            ind+=1
    return render(request,'result.html',{'lr':l})
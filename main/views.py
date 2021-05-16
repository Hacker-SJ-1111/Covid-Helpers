from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Helps,reports,delete
from django.conf import settings
import random
from django.core.files import File
# Create your views here.
def home(request):
    if request.method == "POST":
        Requirement = request.POST.get('Requirement', None)
        city = request.POST.get('city', None)
        Requirement = Requirement.lower()
        city = city.lower()
        allhelps = Helps.objects.all()
        helps = []
        for i in allhelps:
            if i.city.lower() in city or i.state.lower() in city or city in i.city.lower() or city in i.state.lower():
                if i.helps.lower() == Requirement:
                    helps.append(i)
        context = {"All":helps}
        return render(request,"home.html",context)
    allHelps = Helps.objects.all()
    allHelps = list(allHelps)
    random.shuffle(allHelps)
    context = {"All":allHelps}
    return render(request,"home.html",context)

def addhelp(request):
    return render(request,"add help.html")

def newhelp(request):
    personname = request.POST.get('name', None)
    helpobj = request.POST.get('help', None)
    city = request.POST.get('city', None)
    state = request.POST.get('state', None)
    phone = request.POST.get('phone', None)
    NewHelp = Helps(name=personname,helps=helpobj,city=city,state=state,contact=phone)
    NewHelp.save()
    return JsonResponse({})

def report(request):
    pkCode = request.POST.get('pk', None)
    NewReport = reports(pkCode=pkCode)
    NewReport.save()
    return JsonResponse({})

def delete(request):
    print("we are here")
    pkCode = request.POST.get('pk', None)
    reason = request.POST.get('reason', None)
    NewDelete = delete(pkCode=pkCode,reason=reason)
    NewDelete.save()
    print("we are now here")
    return JsonResponse({})

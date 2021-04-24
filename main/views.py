from django.shortcuts import render
from django.http import JsonResponse
from .models import Helps
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
            if i.city.lower() == city or i.state.lower() == city:
                if i.helps.lower() == Requirement:
                    helps.append(i)
        context = {"All":helps}
        return render(request,"home.html",context)
    allHelps = Helps.objects.all()
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
from django.shortcuts import render, redirect
from .models import NGO

def indexpage(request):
    return render(request, "index.html")
def servicepage(request):
    return render(request, "service.html")

def productpage(request):
    return render(request, "product.html")
def partnership(request):
    data = NGO.objects.all()
    context = {"data": data}
    return render(request, "partnership.html", context)

def aboutpage(request):

    return render(request, "about.html")


def signup(request):

    data = NGO.objects.all()
    context = {"data": data}
    return render(request, "signup.html", context)
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        country = request.POST.get('country')
        sdgs = request.POST.get('sdgs')
        directors = request.POST.get('directors')
        members = request.POST.get('members')
        funding = request.POST.get('funding')

        query = NGO(name=name, city=city, country=country, sdgs=sdgs, directors=directors, members=members, funding=funding)
        query.save()
    return redirect("/")


def index(request):
    data = NGO.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def deleteData(request, id):
    d = NGO.objects.get(id=id)
    d.delete()
    return redirect("/partnership")

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        country = request.POST.get('country')
        sdgs = request.POST.get('sdgs')
        directors = request.POST.get('directors')
        members = request.POST.get('members')
        funding = request.POST.get('funding')

        edit = NGO.objects.get(id=id)
        edit.name = name
        edit.city = city
        edit.country = country
        edit.sdgs = sdgs
        edit.directors = directors
        edit.members = members
        edit.funding = funding
        edit.save()
        return redirect("/partnership")
    d = NGO.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html', context)


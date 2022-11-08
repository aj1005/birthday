from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . models import *
# Create your views here.
def home(request):
  wis=wishes.objects.all()
  return render (request,"index.html",{"wis":wis})
def upload(request):
  if request.method=='POST':
    nm=request.POST['name']
    
    cmt=request.POST['cmt']
    wish=wishes(name=nm,message=cmt)
    wish.save()
    if "img" in request.FILES:
      fl=request.FILES['img']
      wish.image=fl
      wish.save()
    return redirect("home")
  
  return render(request,"upload.html")
    
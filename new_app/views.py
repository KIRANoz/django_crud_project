from django.shortcuts import render

from new_app.forms import Furniture, FurnitureForm


def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def dash(request):
    return render(request,'dash.html')
def furniture(request):
    form =FurnitureForm()
    print(form)
    return render(request,'temp.html',{'form':form})

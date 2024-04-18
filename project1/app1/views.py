from django.shortcuts import render,HttpResponse
from .models import Employee

# Create your views here.
def display(request):
    emp=Employee.objects.all()
    context={"emp":emp}
    return render(request,"index.html",context)

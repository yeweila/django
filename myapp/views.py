from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"myapp/index.html")
def index(request):
    return render(request, "myapp/index.html")

def add(request):
    if request.method =="GET":
        a= request.GET["a"]
        b = request.GET["b"]
        Result = int(a)+int(b)
        return JsonResponse({"ret":Result})
    else:
        a=request.POST['a']
        b= request.POST['b']
        result=int(a)+int(b)
        return JsonResponse({"ret":result})
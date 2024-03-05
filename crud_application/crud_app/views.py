from django.shortcuts import render
from crud_app.models import UserTable
from django.http import HttpResponse,JsonResponse
from crud_app.forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from . import forms 


def ShowHttpResponse(request):
    users = UserTable.objects.all().values()
    return HttpResponse(users)
    
def ShowJsonResponse(request):
    '''users = list(UserTable.objects.all().values())    alternate method
    return JsonResponse(users,safe=False)'''
    users = list(UserTable.objects.all().values())
    data = {'users':users}
    return JsonResponse(data)

def ShowParticularIdData(request,id):
    user= UserTable.objects.filter(id=id).values('emp_name','emp_id')
    users= list(user)
    uniqueData = {'users':users}
    return JsonResponse(uniqueData)

def UserFormView(request):  
    users = UserTable.objects.all().values()
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse({"User Added Successful"})
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'test.html',{'form':form})  

def updateData(request,id):
    users = UserTable.objects.get(id=id)
    if request.method == "POST":  
        form = UserForm(request.POST,instance=users)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse({"Updated Successful"})
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'test.html',{'form':form})  

def deleteData(request,id):
    existing_user = UserTable.objects.filter(id=id)
    existing_user.delete()
    return HttpResponse("User Deleted")

    
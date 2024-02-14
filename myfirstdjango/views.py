from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import usersForm
from service.models import Feedback,Featuredcars

def homePage(request):
    feedback_data = Feedback.objects.all().order_by('-name')
    cars_data = Featuredcars.objects.all().order_by('car_price')
    data = {
        'feedbacks' : feedback_data,
        'featured_cars' : cars_data 
    }
    return render(request,'index.html',data)

def services(request):
    finalAns = 0
    fn = usersForm()
    data = {'form':fn}
    try:
        if request.method =="POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            finalAns = n1+n2+n3
            data = {
                'form':fn,
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'output':finalAns
            }
            url = "/contact/?output={}".format(finalAns)
            return redirect(url)
    except:
        pass
    return render(request,'services.html',data)

def contact(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request,'index.html',{'output':output})


def calculator(request):
    c =""
    values ={}
    try:
        if request.method =="POST":
            num1 = eval(request.POST.get('num1'))
            opr = request.POST.get('opr')
            num2 = eval(request.POST.get('num2'))
            if opr == '+':
                c = num1 + num2
            elif opr == '-':
                c = num1 - num2
            elif opr == '*':
                c = num1*num2
            elif opr =='/':
                if num2 != 0:
                   c =  num1/num2
                else:
                    c = "infinity"
        values = {
        'n1': num1,
        'n2': num2,
        'op' : opr,
        'result':c
        }
    except:
        c = "Please enter numbers"
    
    
    return render(request,'calculator.html',values)


from django.shortcuts import render
from django.http import HttpResponse

def carrydata(request,data):
    return HttpResponse(f'<h1> this is myapp response this carry {data} to backend </h1>')

# Create your views here.
def carry(request,sample):
    fact=1
    for i in range(int(sample),1,-1):
        fact=fact*i
    return HttpResponse(f'<h1> display the user input is {sample} to factorial value {fact} </h1>')

def add(request,a,b,c):
    d=int(a)+int(b)+int(c)
    return HttpResponse(f'<h1> after adding the {a},{b},{c} values, final result is {d}</h1>')

def sub(request,a,b,c):
    d=int(a)-int(b)-int(c)
    return HttpResponse(f'<h1> after substracting the {a},{b},{c} values, final result is {d}</h1>')

def factorial(request,sample):
    fact = 1
    for i in range(int(sample),1,-1):
        fact = fact * i
    a={'factvalue':fact,'sample':sample,'list1':['helloworld','haii','pyspider',10,20,30]}
    return render(request,'sample.html',context={'a':a})
    #return render(request,"sample.html",context={'factvalue':fact,'sample':sample})

def fact(request,sample1):
    return render(request,"sample.html")

def login(request,email,password):
    a={"home":["home","ghar","illu","mane","inti"],"aboutus":"hello world"}
    return render(request,"home1.html",{"username":email,"pass":password,"a":a})
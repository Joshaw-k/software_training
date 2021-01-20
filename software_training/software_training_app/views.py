from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'index.html',context)

def about_us(request):
    context = {}
    return render(request,'about.html',context)    

def team_detail(request):
    context = {}
    return render(request,'team-detail.html',context)

def service_detail(request):
    context = {}
    return render(request,'service-detail.html',context)

def teacher(request):
    context = {}
    return render(request,'teachers.html',context) 

def menu(request):
    context = {}
    return render(request,'menu.html',context)     

def blog(request):
    context = {}
    return render(request,'blog.html',context)      

def team(request):
    context = {}
    return render(request,'team.html',context)      

def gallery(request):
    context = {}
    return render(request,'gallery.html',context)      
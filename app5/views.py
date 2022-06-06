from django.shortcuts import render

def home(request):
    return render(request,'temp5/home.html')
    
def kerala(request):
    return render(request,'temp5/kerala.html')

def goa(request):
    return render(request,'temp5/goa.html')    

def rajasthan(request):
    return render(request,'temp5/rajasthan.html')

def kolkkatha(request):
    return render(request,'temp5/kolkkatha.html')

def KASHMIR(request):
    return render(request,'temp5/kashmir.html')

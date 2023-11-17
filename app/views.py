from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This Data Is Our Assumption'
    d={'Assumption':data}
        
    return render(request,'data_render.html',context=d)


def login(request):
    d={'name':'venky','age':'23'}

    return render(request,'login.html',context=d)
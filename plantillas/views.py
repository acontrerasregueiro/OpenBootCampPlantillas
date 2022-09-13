from django.shortcuts import render

def simple(request):
    return render(request,'simple.html',{})

def dinamico(request,name):
    #El contexto es un diccionario
    contexto = {'name' : name}
    return render(request,'dinamico.html',contexto)
    
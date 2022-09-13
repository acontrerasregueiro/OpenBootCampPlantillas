from django.shortcuts import render

def simple(request):
    return render(request,'simple.html',{})

def dinamico(request,name):
    #El contexto es un diccionario
    #Se podrían pasar objetos y por lo sus métodos.
    categories = ['code','design','seo','business']
    contexto = {'name' : name,'categories': categories}
    return render(request,'dinamico.html',contexto)
    
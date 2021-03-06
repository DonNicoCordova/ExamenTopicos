from django.shortcuts import render
from core.models import Contacto
# Create your views here.
def Index(request):
    data = {}
    template_name = 'Index.html'
    return render(request,template_name,data) 

def contactos(request):
    data = {}
    template_name = 'contactos.html'
    contactos = Contacto.objects.all()
    data["contactos"] = contactos
    return render(request,template_name,data) 

def detalles_contacto(request,pk):
    data = {}
    contacto = Contacto.objects.get(pk=pk)
    data['contacto'] = contacto
    template_name = 'detalles_contacto.html'
    return render(request,template_name,data) 
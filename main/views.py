from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.pasteles import pasteles
from main.forms import FormPresupuesto


def indice(req):
  context = {'productos': pasteles}
  return render(req, 'index.html', context)

def about(req):
  return render(req, 'about.html')
def welcome(req):
  return render(req, 'welcome.html')

def contact_form (req):
  customer_name = req.POST['customer_name']
  customer_email = req.POST['customer_email']
  message = req.POST['message']

  errores = []

  if not '@' in customer_email:
    errores.append('Debe poseer un arroba')

  if len(customer_name) >=64:
    errores.append('Debe ser menor a 64 caracteres')
  if len(customer_name) <=1:
    errores.append('El nombre ingresado no es real')
  context ={'errores': errores}
  if len(errores) >0:
    return render(req, 'welcome.html', context)
  else:
    return render(req,'respuesta.html', context)
def presupuesto (req):
    if req.method == 'GET':
      form= FormPresupuesto()
      context = {'form':form}
      return render(req,'presupuesto.html', context)
    else:
      form = FormPresupuesto (req.POST)
      if form.is_valid():
        return redirect('/exito')
      
    
def exito(req):
  return HttpResponse('Exito')
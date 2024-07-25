from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.pasteles import pasteles
from main.forms import FormPresupuesto as PresupuestoForm
from main.models import FormPresupuesto, Flan
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

class LoginViewPropia(SuccessMessageMixin, LoginView):
  success_message = "Has ingresado correctamente"
  

def indice(req):
  context = {'productos': pasteles}
  return render(req, 'index.html', context)

def about(req):
  return render(req, 'about.html')
def welcome(req):
  return render(req, 'welcome.html')
def timeline (req):
  return render (req, 'timeline.html')

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
  
@login_required
def presupuesto (req):
    if req.method == 'GET':
      form = PresupuestoForm()
      context = {'form':form}
      return render(req,'presupuesto.html', context)
    else:
      form = PresupuestoForm (req.POST)
      if form.is_valid():
        FormPresupuesto.objects.create(
        **form.cleaned_data
      )
        return redirect('/exito')
      
    
def exito(req):
  return redirect('/index.html')


def flanes(req):
    all_flans = Flan.objects.all()
    context = {'flans' : all_flans}
    return render(req, 'flanes.html' ,context )

def privados(req):
    all_flans = Flan.objects.filter(is_private=True)
    context = {'all_flans' : all_flans}
    return render(req, 'flanes18.html' ,context )

def agregar_usuarios(req):
    nuevo_usuario = req.POST['usuario']
    usuario.append(nuevo_usuario)
    return redirect('/')
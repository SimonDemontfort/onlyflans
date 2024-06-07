from django.urls import path
from main.views import contact_form, indice, about, welcome, presupuesto, exito

urlpatterns = [
  path('', indice),
  path('about/', about),
  path('welcome/', welcome),
  path('contact_form',contact_form, name='contact_form'),
  path('presupuesto/',presupuesto),
  path('exito', exito)

  
]
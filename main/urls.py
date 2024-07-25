from django.urls import path, include
from main.views import contact_form,flanes,privados, indice, about, welcome, presupuesto, exito, LoginViewPropia
from django.contrib import admin

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', indice),
  path('accounts/login/', LoginViewPropia.as_view()),
  path('about/', about),
  path('welcome/', welcome),
  path('contact_form',contact_form, name='contact_form'),
  path('presupuesto/',presupuesto),
  path('exito', exito),
  path('flanes/',flanes, name= "all_flanes"),
  path('flanes18/',privados, name= "all_flanes18")

  
]
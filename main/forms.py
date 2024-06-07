from django import forms

class FormPresupuesto(forms.Form):
    nombre = forms.CharField(max_length=64,
    widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    correo = forms.EmailField(max_length=30,
    widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    productos = forms.CharField(max_length=260,
    widget=forms.TextInput(attrs={'class': 'form-control'})
    )
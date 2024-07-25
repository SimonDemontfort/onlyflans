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
class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label='Nombre:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese nombre aquí'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese correo aquí'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje:',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3 fst-italic',
            'rows': 5,
            'placeholder': 'Ingrese mensaje. Máximo 500 carácteres'
        })
    )
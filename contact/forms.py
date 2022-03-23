from django import forms


class FormularioContacto(forms.Form):
    name = forms.CharField(label='name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'}))
    email = forms.EmailField(label='correo', required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your e-mail here'}))
    cell = forms.CharField(label='cellphone', required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number here'}))
    asunto = forms.CharField(label='subject', required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter a subject here'}))
    mensaje = forms.CharField(label='consulta', required=True, widget=forms.Textarea(attrs={'placeholder': 'Write your message here'}))
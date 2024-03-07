from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, ResetPasswordKeyForm
from django import forms
from django.core.validators import MinLengthValidator
from django.forms.widgets import ClearableFileInput
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(SignupForm):
    email = forms.EmailField(required=True, label='Email', 
                            widget=forms.EmailInput(attrs={'class': 'email-field'}))
    nome_completo = forms.CharField(validators=[MinLengthValidator(10)], max_length=120) 
    telefone_celular = forms.IntegerField(label='Telefone celular', 
                                          widget=forms.TextInput(attrs={'class': 'telefone-field'}),
                                          required=True)

                            
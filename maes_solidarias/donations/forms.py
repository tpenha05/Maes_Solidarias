from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'phone_number', 'birth_date', 'cpf', 'amount', 'periodicity']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.Select(),
            # 'amount': forms.RadioSelect(choices=Donation.AMOUNT_CHOICES),
            'periodicity': forms.Select(),
        }

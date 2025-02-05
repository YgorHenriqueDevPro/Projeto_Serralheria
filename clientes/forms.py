from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("A senha deve ter no mínimo 6 caracteres.")
        return password

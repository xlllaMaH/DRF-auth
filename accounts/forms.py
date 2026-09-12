from django import forms
from django.contrib.auth import get_user_model
from users.models import CustomUserModel

User = get_user_model()

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput)
    username = forms.CharField(max_length=25, required=False,)

    class Meta:
        model = CustomUserModel
        fields = [
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
            'password_confirm'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("password_confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Пароли не совпадают!")

        return cleaned_data
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from User.models import Customer


class RegistrationForm(UserCreationForm):
    email =  forms.EmailField(max_length=255,help_text="Required. Add a valid email.")

    class Meta:
        model   = Customer
        fields  = ('email','username','password1','password2')

    def clean_email(self):
        email   = self.cleaned_data['email'].lower()
        print(email)
        try:
            customer  = Customer.objects.get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def clean_username(self):
        username   = self.cleaned_data['username']
        print(username)
        try:
            customer  = Customer.objects.get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use.")
    
class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Customer
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")
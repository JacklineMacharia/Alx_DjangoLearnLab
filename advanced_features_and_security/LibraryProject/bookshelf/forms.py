from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, help_text="Enter your full name")
    email = forms.EmailField(required=True, help_text="Enter a valid email address")
    message = forms.CharField(widget=forms.Textarea, required=True, help_text="Enter your message")
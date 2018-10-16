from django import forms

from django.contrib.auth import authenticate,get_user_model
User=get_user_model()
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        usern = self.cleaned_data.get("username")
        passw = self.cleaned_data.get("password")
        val = authenticate(username=usern, password=passw)
        if val is None:
            raise forms.ValidationError("user doesnot exists")
        if not val.check_password(passw):
            raise forms.ValidationError("password is not correct")

class OrderForm(forms.Form):
    qty=forms.IntegerField()

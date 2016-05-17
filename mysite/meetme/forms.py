from django import forms

# Create your forms here.


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=24)
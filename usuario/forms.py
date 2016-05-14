from django import forms


class form_user(forms.Form):
        email = forms.EmailField(
            max_length=200
        )
        password = forms.CharField(
            min_length=6,
            max_length=100,
            widget=forms.PasswordInput
        )

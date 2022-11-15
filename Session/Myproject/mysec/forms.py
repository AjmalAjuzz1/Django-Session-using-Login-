from django import forms

GENDER=[('Male','Male'), ('Female','Female'),('Others','Others')]

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        required=True,
    )
    name= forms.CharField(
        max_length=100,
        required=True,
    )
    age= forms.IntegerField()

    gender= forms.CharField(
        label='Gender',
        widget=forms.RadioSelect(choices=GENDER),
    )
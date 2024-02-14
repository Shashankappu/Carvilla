from django import forms

class usersForm(forms.Form):
    num1 = forms.CharField(label="Num1",widget=forms.TextInput(attrs={'class':"flow-control"}))
    num2 = forms.CharField(label="Num2")
    num3 = forms.CharField(label="Num3")
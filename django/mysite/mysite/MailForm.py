from django import forms
 
class MailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    address1 = forms.CharField(label='Address', max_length=50)
    address2 = forms.CharField(label='Address2', max_length=50, required=False)
    postalcode = forms.CharField(label='Postal code', max_length=10)

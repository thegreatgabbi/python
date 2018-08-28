from django.forms import ModelForm
from mysite.inventory.models import Customer
 
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['cid','name','products']
 
    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)

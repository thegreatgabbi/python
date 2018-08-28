from django.http.response import HttpResponse
from django.core import serializers
import json
from django.template import Template
from django.shortcuts import render, redirect
from mysite.inventory.CustomerForm import CustomerForm
from mysite.inventory.models import Customer

def customers(request):
    allcust = Customer.objects.all()
    if request.GET.get('json', None) is None:
        return render(request, 'customers.html', { 'customers' : allcust })
    else:
        ser = serializers.serialize('json', allcust)
        py = json.loads(ser)
        py = list(map((lambda x: x['fields']), py))
        ser = json.dumps(py)
        return HttpResponse(ser, content_type="application/json")
 
def customer(request, custid):
    try:
        c = Customer.objects.get(cid=custid)
        if request.GET.get('json', None) is None:
            return render(request, 'customer.html', {'customer':c})
        else:
            ser = serializers.serialize('json', [ c ])
            py = json.loads(ser)
            ser = json.dumps(py[0]['fields'])
            return HttpResponse(ser, content_type="application/json")
    except Exception as e:
        t = Template("""<html><body>
                     Customer {{ c }} not found
                     </body></html>""")
        html = t.render({'c':custid })
        return HttpResponse(html)
 
def editCustomer(request, custid):
    cust = Customer.objects.get(cid=custid)
    if request.method == "GET":
        form = CustomerForm(instance=cust)
    elif request.method == "POST":
        form = CustomerForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('../customer')
    form.fields['cid'].widget.attrs['readonly'] = True
    return render(request, 'custform.html', {'myform': form})
 
def addCustomer(request):
    if request.method == "GET":
        form = CustomerForm()
    elif request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./customer')
    return render(request, 'custform.html', {'myform': form})

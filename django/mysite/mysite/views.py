import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from mysite.MailForm import MailForm

def home(request):
    dt = datetime.datetime.now()
    html = '''
<html><body><h1>From django</h1>
<p>Time now: {}.
</body></html>'''.format(dt)
    return HttpResponse(html)
 
def sayhi(request, name):
    context = {'name':name, 'location':'Singapore'}
    html = get_template('sayhi.html').render(context)
    return HttpResponse(html)

def getAddress(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f = MailForm(request.POST)
        # check whether it's valid:
        if f.is_valid():
            # process the data in form.cleaned_data as required
            html = '<html><body>%s<br>%s<br>%s<br>%s</body></html>' % (
                         f.cleaned_data['name'],
                         f.cleaned_data['address1'],
                         f.cleaned_data['address2'],
                         f.cleaned_data['postalcode'])
            return HttpResponse(html)
    else:
        # GET method -- create a blank form
        f = MailForm()
    return render(request, 'mailform.html', {'myform': f})

from django.urls import path
from django.urls import re_path
from mysite.inventory import views
 
urlpatterns = [
    path('customer', views.customers),
    re_path('^customer/(.+)$', views.customer),
    re_path('^editcust/(.+)$', views.editCustomer),
    path('addcust', views.addCustomer),
]

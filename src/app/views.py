from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from datetime import datetime,timedelta
from django.views.generic import TemplateView
from django.core import serializers
from .forms import ClientForm
from .models import Client,Payment
import json
# Create your views here.


def home_view(request,url):
    context = {
        'url':url
    }
    return render(request,'home.html',context=context)


class FormView(TemplateView):
    template_name = 'form.html'
    form_class = ClientForm

    def get_context_data(self):
        context = super(FormView,self).get_context_data()
        context['form'] = ClientForm()
        return context

    def post(self,request):
        form = self.form_class(request.POST)
        print(form.data)
        form.save()
        if form.is_valid():
            return redirect('/home/')
        else:
            return HttpResponse("not submitted")

def paid_payments(req):
    filter_date = datetime.today() - timedelta(days=60)
    data = Payment.objects.filter(payment_date__gt=filter_date,status='paid')
    data_list = serializers.serialize('json', data)
    data_list = json.loads(data_list)
    
    res = []
    # print(data_list)
    for item in data_list:
        dic = {}
        id = item['fields']['user']
        dic['amount'] = item['fields']['paid_amount']
        user = Client.objects.get(pk=id)
        print(user)
        dic['user'] = str(user)
        dic['status'] = item['fields']['status']
        dic['date'] = item['fields']['payment_date']
        res.append(dic)
    print(res)
    data = {
    "rows":res
    }
    return JsonResponse(data,safe=False)

def open_payments(req):
    filter_date = datetime.today() - timedelta(days=60)
    data = Payment.objects.filter(payment_date__gt=filter_date,status='open')
    data_list = serializers.serialize('json', data)
    data_list = json.loads(data_list)
    
    res = []
    # print(data_list)
    for item in data_list:
        dic = {}
        id = item['fields']['user']
        dic['amount'] = item['fields']['paid_amount']
        user = Client.objects.get(pk=id)
        print(user)
        dic['user'] = str(user)
        dic['status'] = item['fields']['status']
        dic['date'] = item['fields']['payment_date']
        res.append(dic)
    print(res)
    data = {
    "rows":res
    }
    return JsonResponse(data,safe=False)

def all_payments(req):
    filter_date = datetime.today() - timedelta(days=60)
    data = Payment.objects.filter(payment_date__gt=filter_date)
    data_list = serializers.serialize('json', data)
    data_list = json.loads(data_list)
    
    res = []
    # print(data_list)
    for item in data_list:
        dic = {}
        id = item['fields']['user']
        dic['amount'] = item['fields']['paid_amount']
        user = Client.objects.get(pk=id)
        print(user)
        dic['user'] = str(user)
        dic['status'] = item['fields']['status']
        dic['date'] = item['fields']['payment_date']
        res.append(dic)
    print(res)
    data = {
    "rows":res
    }
    return JsonResponse(data,safe=False)
def home(r):
  
    filter_date = datetime.today() - timedelta(days=60)
    data = Client.objects.filter(timestamp__gt=filter_date)
    data_list = serializers.serialize('json', data)
    data_list = json.loads(data_list)
    
    res =[]
    for item in data_list:
        dic = {}
        dic['id'] = item['pk']
        dic['name'] = item['fields']['name']
        dic['number'] = item['fields']['primary_number']
        res.append(dic)
    data = {
        "rows":res
    }
    return JsonResponse(data,safe=False)
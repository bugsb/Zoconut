from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from datetime import datetime,timedelta
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .helper import parse_payment_data,parse_client_data
from .forms import ClientForm
from .models import Client,Payment

def home_view(request,url):
    context = {
        'url':url,
        'id':request.GET.get('user')
    }
    return render(request,'home.html',context=context)

class FormView(TemplateView):
    template_name = 'form.html'
    form_class = ClientForm

    def get_context_data(self):
        context = super(FormView,self).get_context_data()
        context['form'] = ClientForm()
        return context

    def post(self,request,user):
        form = self.form_class(request.POST)
        print(form.data)
        form.save()
        if form.is_valid():
            return redirect(f'/app/home/all_payments?user={user}')
        else:
            return HttpResponse("not submitted")

def paid_payments(request):
    user_id = request.GET.get('user')
    filter_date = datetime.today() - timedelta(days=60)
    data = Payment.objects.all().select_related('filtering_id').filter(filtering_id__user__id=user_id,payment_date__gt=filter_date,status='paid')
    response = parse_payment_data(data)
    return JsonResponse(response,safe=False)

def open_payments(request):
    user_id = request.GET.get('user')
    filter_date = datetime.today() - timedelta(days=60)
    data = Payment.objects.all().select_related('filtering_id').filter(filtering_id__user__id=user_id,payment_date__gt=filter_date,status='open')
    response = parse_payment_data(data)
    return JsonResponse(response,safe=False)

def all_payments(request):
    user_id = request.GET.get('user')
    filter_date = datetime.today() - timedelta(days=60)
    data = Payment.objects.all().select_related('filtering_id').filter(filtering_id__user__id=user_id)
    response = parse_payment_data(data)
    return JsonResponse(response,safe=False)

def clients_added(r,user_id):
    filter_date = datetime.today() - timedelta(days=60)
    data = Client.objects.all().select_related('filtering_id').filter(timestamp__gt=filter_date,filtering_id__user__id=user_id)
    data = parse_client_data(data)
    return JsonResponse(data,safe=False)
from .models import *
from datetime import datetime,timedelta
from django.db.models import Sum
filter_date = datetime.today() - timedelta(days=60)

def account_holder(request):
    account_holder = AccountHolder.objects.all()[0]
    return {'account_holder':account_holder}

def clients(request):
    filter_date = datetime.today() - timedelta(days=60)
    clients_count = Client.objects.filter(timestamp__gt=filter_date).count()
    clients_basic_info = Client.objects.filter(basic_info_status=True).count()
    return {'client_count':clients_count,'client_basic_info':clients_basic_info}

def appointments(request):
    filter_date = datetime.today() - timedelta(days=60)
    appointment_count = Appointment.objects.filter(payment_date__gt=filter_date).count()
    
    return {'appointments_count':appointment_count}
def payments(request):
    payments = Payment.objects.filter(payment_date__gt=filter_date).aggregate(Sum('paid_amount'))
    
    return {'payments':payments['paid_amount__sum']}
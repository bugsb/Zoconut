from .models import *
from django.db.models import Sum
from django.contrib.auth.models import User
from .helper import get_past_date

def account_holder(request):
    user_id = request.GET.get('user')
    account_holder = User.objects.select_related('accountholder').filter(
        id=user_id).first()

    return {'account_holder':account_holder}

def clients(request):
    user_id = request.GET.get('user')
    filter_date = get_past_date(days=60)
    clients_count = Client.objects.select_related().filter(
        timestamp__gt=filter_date,filtering_id__user__id=user_id).count()

    clients_basic_info = Client.objects.select_related().filter(
        basic_info_status=True,filtering_id__user__id=user_id).count()

    return {'client_count':clients_count,'client_basic_info':clients_basic_info}

def appointments(request):
    user_id = request.GET.get('user')
    filter_date = get_past_date(days=60)
    appointment_count = Appointment.objects.select_related().filter(
        payment_date__gt=filter_date,filtering_id__user__id=user_id).count()

    return {'appointments_count':appointment_count}
    
def payments(request):
    user_id = request.GET.get('user')
    filter_date = get_past_date(days=60)
    payments = Payment.objects.select_related().filter(
        payment_date__gt=filter_date,filtering_id__user__id=user_id).aggregate(Sum('paid_amount'))
        
    return {'payments':payments['paid_amount__sum']}
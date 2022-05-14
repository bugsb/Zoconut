from datetime import datetime,timedelta
from django.core import serializers
from .models import Client
import json

def parse_payment_data(data):
    json_data = json_serialize(data)
    result = []
    for item in json_data:
        data_dict = {}
        id = item['fields']['user']
        data_dict['amount'] = item['fields']['paid_amount']
        user = Client.objects.get(pk=id)
        data_dict['user'] = str(user)
        data_dict['status'] = item['fields']['status']
        data_dict['date'] = item['fields']['payment_date']
        result.append(data_dict)

    return result

def parse_client_data(data):
    json_data = json_serialize(data)
    result = []
    for item in json_data:
        data_dict = {}
        data_dict['id'] = item['pk']
        data_dict['name'] = item['fields']['name']
        data_dict['number'] = item['fields']['primary_number']
        result.append(data_dict)

    return result

def json_serialize(data):
    data_list = serializers.serialize('json', data)
    json_data = json.loads(data_list)
    return json_data

def get_past_date(days):
    past_date = datetime.today() - timedelta(days=days)
    return past_date
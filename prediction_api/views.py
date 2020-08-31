from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from prediction_api.api import predicate
from pprint import pprint
from .models import ApplicationData
from django.db import IntegrityError

def index(request):    
    data = predicate.get_current_values()
    data = data.json()
    data_points = data['result']['dataPoints']['APPLICATION-294916C9639A9385']
    for dp in data_points:
        timestamps = dp[0]
        data_point = dp[1]        
        add_or_update_data_points_to_db(timestamps, data_point)        
    return HttpResponse("Added Data Points")


def add_or_update_data_points_to_db(timestamp, data_point):
    try:
        applicationdata, created = ApplicationData.objects.update_or_create(
            timestamp=timestamp, defaults={"data_point": data_point}
        )
    except IntegrityError:
        applicationdata, created = ApplicationData.objects.update_or_create(
            timestamp=timestamp, defaults={"data_point": 0}
        )    

def add_datapoints_to_db(timestamp, data_point):
    try:
        applicationData = ApplicationData()
        applicationData.timestamp = timestamp
        applicationData.data_point = data_point
        applicationData.save()        
    except IntegrityError:
        applicationData = ApplicationData()
        applicationData.timestamp = timestamp
        applicationData.data_point = 0
        applicationData.save()

from django.shortcuts import render,get_object_or_404
from .models import dayofweek
from .serializers import DaySerializer
from django.http import JsonResponse

def getmsg(request,day_id):
    selected_day = get_object_or_404(dayofweek,pk=day_id)
    serializer = DaySerializer(selected_day,many=False)
    return JsonResponse(serializer.data,safe=False)

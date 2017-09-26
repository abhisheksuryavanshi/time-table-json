from rest_framework import serializers
from .models import dayofweek

class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = dayofweek
        fields = '__all__'
        #fields = ('company_name','volume')

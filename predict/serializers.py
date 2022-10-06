from rest_framework import serializers
from predict.models import *

class HomePageSerializer(serializers.ModelSerializer):
    class __meta__:
        model = CleanedData
        fields = '__all__'
from rest_framework.serializers import ModelSerializer
from .models import plan,Operator,Region,recharge
from rest_framework import serializers

class planSerializer(ModelSerializer):
    class Meta:
        model= plan
        fields= ['rupees','operator','region','data','validity']


class OperatorSerializer(ModelSerializer):
    class Meta:
        model= Operator
        fields= ['id','name']


class RegionSerializer(ModelSerializer):
    class Meta:
        model= Region
        fields= ['id','operator','rname']


class rechargeSerializer(ModelSerializer):
  class Meta:
    model = recharge
    fields = ['id','mobile','price','Plan']
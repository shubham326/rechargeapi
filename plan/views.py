from django.shortcuts import render
from .models import plan,Operator,Region,recharge
from .serializers import planSerializer,OperatorSerializer,RegionSerializer,rechargeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class planListCreateAPIView(ListCreateAPIView):
    serializer_class=planSerializer
    queryset=plan.objects.all()
class planRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=planSerializer
    queryset=plan.objects.all()
    lookup_field='id'

class OperatorListCreateAPIView(ListCreateAPIView):
    serializer_class=OperatorSerializer
    queryset=Operator.objects.all()
class planRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=OperatorSerializer
    queryset=Operator.objects.all()
    lookup_field='id'

class RegionListCreateAPIView(ListCreateAPIView):
    serializer_class=RegionSerializer
    queryset=Region.objects.all()
class planRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=RegionSerializer
    queryset=Region.objects.all()
    lookup_field='id'

class rechargeListCreateAPIView(ListCreateAPIView):
  serializer_class = rechargeSerializer
  queryset = recharge.objects.all()
class rechargeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=rechargeSerializer
    queryset=recharge.objects.all()
    lookup_field='id'
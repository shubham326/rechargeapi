from django.contrib import admin
from django.urls import path
from plan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plan/', planListCreateAPIView.as_view()),
    path('op/', OperatorListCreateAPIView.as_view()),
    path('re/', RegionListCreateAPIView.as_view()),
    path('recharge/', rechargeListCreateAPIView.as_view()),
    path('recharge/<int:id>/', rechargeRetrieveUpdateDestroyAPIView.as_view()),
]


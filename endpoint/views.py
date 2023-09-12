from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EndpointSerializer
from .models import Endpoint
from django.http import JsonResponse
from rest_framework.routers import SimpleRouter







class DesView(APIView):


    def get(self, request, *args, **kwargs):

        api_uls = {
        'all_items': '/?api',
		'Search by Slack': '/?slack_name=slack_name',
		'Search by Track': '/?track=track',
        }
        return JsonResponse(api_uls)
    

    def get(self, request, *args, **kwargs):
        query = Endpoint.objects.all()
        serializers = EndpointSerializer(query, many=True)
       
       
        return JsonResponse(serializers.data)
    
   

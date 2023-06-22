from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Advocates

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    # data = ['Lumar', 'Tadas', 'Plato']
    advocates = Advocates.objects.all()
    return Response(data)
    
@api_view(['GET'])
def advocates_detail(request, username):
    data = username
    return Response(data)
    
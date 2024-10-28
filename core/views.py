from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class TestView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})
    
    def post(self, request):
        print(request.data)
        return Response({'message': 'Posting hello world!'})

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class test(APIView):
    # def get_queryset(self):
    #     return 'hello'
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response('hi', status=status.HTTP_200_OK)

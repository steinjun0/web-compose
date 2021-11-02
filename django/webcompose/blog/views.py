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
        # f = open('./temp.py', 'w')
        # f.write("print('hello')")
        # f.close()
        # exec(open('./temp.py').read())
        from . import temp
        result = temp.some_func()
        return Response(result, status=status.HTTP_200_OK)

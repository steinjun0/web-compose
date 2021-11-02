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
    
    def post(self, request, **kargs):
        # print(request.data['value'])
        # print(request.data['value'].read())
        # f = open('./temp.py', 'w')
        # f.write("print('hello')")
        # f.close()
        # exec(open('./temp.py').read())
        from . import temp
        result = ''
        loc = {}
        exec(request.data['value'].read(), globals(), loc)
        return_workaround = loc['result']
        print(return_workaround)
        return Response(return_workaround, status=status.HTTP_200_OK)

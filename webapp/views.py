# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from webapp.models import Employees
from webapp.serializers import EmployeesSerializer


# Create your views here.


def home(request):
    return render(request, 'webapp/home.html')


#class EmployeeList(APIView):
#       employees = Employees.objects.all()
#        serializer_var =  EmployeesSerializers(Employees, many=True)
#        return Response(serializer_var.data)
#

#    def post(self):
#        pass


@csrf_exempt
def employees_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

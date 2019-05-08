from rest_framework import serializers
from webapp.models import Employees

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ['first_name','last_name']

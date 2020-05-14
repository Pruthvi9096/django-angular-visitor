from rest_framework import serializers
from .models import Department,Visit,VisitFor,Visitor
from django.contrib.auth import get_user_model

User  = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {
            'password':{'write_only':True}
        }

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def validate_department_name(self,department_name):
        qs = Department.objects.filter(department_name__iexact=department_name)
        if qs.exists():
            raise serializers.ValidationError("Department Name Should be Unique")
        else:
            return department_name

class VisitForSerializer(serializers.ModelSerializer):
    # department = serializers.HyperlinkedRelatedField(many=False, view_name='department-detail',read_only=True)
    class Meta:
        model = VisitFor
        fields = '__all__'

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'

class VisitListSerializer(serializers.ModelSerializer):
    visitor_name = VisitorSerializer(many=False)
    visit_to = VisitForSerializer(many=False)
    class Meta:
        model = Visit
        fields = ('id','visitor_name','visit_to','purpose','checkIn_time','checkOut_time')

class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visitor_name','visit_to','purpose','checkIn_time','checkOut_time')
        
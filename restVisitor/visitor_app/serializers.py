from rest_framework import serializers
from .models import Department,Visit,VisitFor,Visitor
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField,EmailField

User  = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    username = CharField()
    email = EmailField(label="Email Address")

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'token',
            )
        extra_kwargs = {
            'password':{'write_only':True}
        }

class UserCreateSerializer(serializers.ModelSerializer):
    password2 = CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('username','email','password','password2')
        extra_kwargs = {
            'password':{'write_only':True},
            # 'password2':{'write_only':True}
        }

    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("Email is already registered")
        if password != password2:
            raise serializers.ValidationError("Password doesn't match with previous password")
        return data


    def create(self,validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        print(validated_data)
        return validated_data

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
        
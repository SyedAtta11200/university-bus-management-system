from rest_framework import serializers
from authentication.serializers import UserSerializer
from authentication.models import User
from .models import Bus

class BusSerializer(serializers.ModelSerializer):
    students = UserSerializer(required=False, many=True)

    class Meta:
        model = Bus
        fields = '__all__'
    
    def create(self, validated_data):
        
        user_data = validated_data.pop('students', [])

        bus_instance = Bus.objects.create(**validated_data)

        for objs in user_data:
            User.objects.create(bus=bus_instance, **objs)
        
        return bus_instance
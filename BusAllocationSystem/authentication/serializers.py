from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, attrs):
        username = attrs['username']

        if not username.isalnum():
            raise serializers.ValidationError("Only alphanumeric characters are allowed in username!")
        
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
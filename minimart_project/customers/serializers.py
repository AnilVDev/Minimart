from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    def validate_email(self, value):
        """Validate email format"""
        if '@' not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        self.validate_email(email)  
        return super().create(validated_data)

    def update(self, instance, validated_data):
        email = validated_data.get('email', instance.email)
        self.validate_email(email)  
        return super().update(instance, validated_data)
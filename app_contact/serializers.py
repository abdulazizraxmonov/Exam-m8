from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()  
    class Meta:
        model = Contact
        fields = ['id', 'firstname', 'email', 'message']

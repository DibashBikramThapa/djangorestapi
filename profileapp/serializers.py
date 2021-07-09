from rest_framework import serializers



class HelloSerializer(serializers.Serializer):
    """serialize name field for test"""
    name = serializers.CharField(max_length=10)

    

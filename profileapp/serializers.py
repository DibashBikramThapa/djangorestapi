from rest_framework import serializers
from profileapp import models


class HelloSerializer(serializers.Serializer):
    """serialize name field for test"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs={
            'password': {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """Create new user"""
        user = models.UserProfile.objects.create_user(
                    email=validated_data['email'],
                    username=validated_data['username'],
                    password=validated_data['password'])
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """profile feed item"""
    class Meta:
        model=models.ProfileFeedItem
        fields=['id','user_profile','status_text','created_on']
        extra_kwargs={'user_profile':{'read_only':True}}

from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    # 직렬화를 통해 장고 레스트 프레임워크로 연속성을 만들 수 있게 된다
    name = serializers.CharField(max_length=10)     # 10보다 적으면 에러

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    class Meta:
        model = models.UserProfile
        # field = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {   # 필드 모델 구성
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        fields = ('id', 'email', 'name', 'password')

    def create(self, validated_data):
        """Create and return a new User"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializers profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

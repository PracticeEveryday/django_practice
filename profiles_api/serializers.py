from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    # 직렬화를 통해 장고 레스트 프레임워크로 연속성을 만들 수 있게 된다
    name = serializers.CharField(max_length=10)     # 10보다 적으면 에러
from rest_framework import serializers
from watchListApp.models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'
class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields = "__all__"
        
        

# def name_length(value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Name must be at least 3 characters long")
        
#         else:
#             return value
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # Field level validation
#     # def validate_name(self, value):
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError("Name must be at least 3 characters long")
        
#     #     else:
#     #         return value
        
#     # Object level validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and Description must be different")
        
#         else:
#             return data
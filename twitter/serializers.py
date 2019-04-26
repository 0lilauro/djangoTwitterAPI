from rest_framework import serializers
from .models import Twitter
from datetime import datetime 

class TwitterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Twitter
        fields = '__all__'

    def create(self,validated_data):
        return Twitter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.post = validated_data.get('post', instance.post)
        instance.id = validated_data.get('id', instance.id)
        instance.date = datetime.now().strftime("%Y-%m-%d")
        instance.save()
        return instance
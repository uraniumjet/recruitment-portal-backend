from rest_framework import serializers
from .models import Job

# class JobSerializer(serializers.ModelSerializer):

#     posted_by = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Job
#         fields = '__all__'
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['posted_by', 'status']

    def create(self, validated_data):
        validated_data['posted_by'] = self.context['request'].user
        validated_data['status'] = 'pending'
        return super().create(validated_data)

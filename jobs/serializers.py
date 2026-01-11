from rest_framework import serializers
from .models import Job


# ================================
# READ SERIALIZER (LIST / DETAIL)
# ================================
class JobListSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'location',
            'salary',
            'job_type',
            'posted_by',
            'created_at',
        ]


# ================================
# WRITE SERIALIZER (CREATE / UPDATE)
# ================================
class JobCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'location',
            'salary',
            'job_type',
        ]

    def create(self, validated_data):
        request = self.context['request']
        validated_data['posted_by'] = request.user
        validated_data['status'] = 'pending'
        return super().create(validated_data)

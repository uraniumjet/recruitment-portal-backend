from rest_framework import serializers
from .models import Application

# class ApplicationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Application
#         fields = '__all__'
#         read_only_fields = ['candidate', 'status']

#     def validate(self, attrs):
#         user = self.context['request'].user

#         if user.role != 'candidate':
#             raise serializers.ValidationError(
#                 "Only candidates can apply for jobs."
#             )

#         return attrs
class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['candidate', 'status']

    def validate_resume(self, file):
        if not file:
            return file

        if file.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Resume size must be under 2MB."
            )

        allowed_types = [
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        ]

        if file.content_type not in allowed_types:
            raise serializers.ValidationError(
                "Only PDF or DOC/DOCX files are allowed."
            )

        return file

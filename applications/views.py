from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsCandidate, IsRecruiterForJob

# Candidate applies to a job
class ApplyToJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def perform_create(self, serializer):
        serializer.save(
            candidate=self.request.user,
            job_id=self.kwargs['job_id']
        )


# Candidate sees own applications
class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            candidate=self.request.user
        )


# Recruiter updates application status
class UpdateApplicationStatusView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsRecruiterForJob]
    http_method_names = ['patch']
    
class ApplyToJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def perform_create(self, serializer):
        serializer.save(
            candidate=self.request.user,
            job_id=self.kwargs['job_id']
        )

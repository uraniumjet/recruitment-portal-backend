from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Job
from .serializers import serializers as JobSerializer
from .permissions import IsRecruiter, IsOwnerOrAdmin
from .pagination import JobPagination
from .filters import JobFilter
from rest_framework.permissions import IsAdminUser

class AdminJobApprovalView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['patch']



class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    pagination_class = JobPagination
    filterset_class = JobFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'salary']
    ordering = ['-created_at']

    def get_queryset(self):
        return Job.objects.filter(
            status='approved'
        ).select_related('posted_by')
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRecruiter()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerOrAdmin]

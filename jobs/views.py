from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Job
# FIXED: Imported the class directly from the serializers file
from .serializers import JobListSerializer
from .permissions import IsRecruiter, IsOwnerOrAdmin
from .pagination import JobPagination
from .filters import JobFilter
from django.shortcuts import get_object_or_404, render

class AdminJobApprovalView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['patch']

class JobListCreateView(generics.ListCreateAPIView):
    """
    Combined View: 
    - GET: List approved jobs (Public)
    - POST: Create a new job (Recruiters only)
    """
    serializer_class = JobListSerializer
    pagination_class = JobPagination
    filterset_class = JobFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'salary']
    ordering = ['-created_at']

    def get_queryset(self):
        # Optimized with select_related to reduce database hits
        return Job.objects.filter(status='approved').select_related('posted_by')

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsRecruiter()]
        return [AllowAny()]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the creator
        serializer.save(posted_by=self.request.user)


def job_detail(request, pk):
    job = get_object_or_404(
        Job.objects.select_related("posted_by"),
        pk=pk
    )

    return render(request, "jobs/job_detail.html", {
        "job": job
    })


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [IsOwnerOrAdmin]
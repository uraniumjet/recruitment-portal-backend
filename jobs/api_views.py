from rest_framework.generics import RetrieveAPIView
from .models import Job
from .serializers import JobSerializer
from .permissions import IsRecruiterOrReadOnly

class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.filter(status='approved')
    serializer_class = JobSerializer
    permission_classes = [IsRecruiterOrReadOnly]
